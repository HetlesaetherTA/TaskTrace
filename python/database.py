import pandas as pd
import os 
import shutil
from random import randint
from datetime import datetime
pd.options.mode.chained_assignment = None

DATABASE_FILE_PATH = "../tasktrace/inventory.csv"
BACKUP_PATH = "../tasktrace/backup"

df = pd.read_csv(DATABASE_FILE_PATH)

class Inventory:
    def currentTime():
        output = ""
        temp = datetime.now() # 2023-04-26 13:13:19.055306
        print(temp)
        temp = str(temp)

        for i in temp:
            try:
                int(i)
                output = output + str(i)
            except:
                pass
        print(output)
        return output # 20230426132305107841
    
    def getProfit():
        for index in range(len(df.columns)):
            for key in df:
                if df["Realized_Gain"].iloc[index] != 0:
                    if key == "Profit" and df["Profit"].iloc[index] == 0:
                        df[key].iloc[index] = df["Realized_Gain"].iloc[index] - df["Buy_Price"].iloc[index] - df["Repair_Cost"].iloc[index]
   
    def save():
        backup_filename = Inventory.currentTime()
        shutil.move(DATABASE_FILE_PATH, BACKUP_PATH + "/" + backup_filename + ".csv")
        df.to_csv(DATABASE_FILE_PATH, index=False)

    def add(model, buy_price, repair_cost, description):
        while True:
            id_number = randint(1000000, 7769999)
            id_number = str(id_number)
            chr_id = int(id_number[0:3])
            id_number = [chr(65 + int((chr_id - 100) / 26)), 0, id_number[2:-1]]
            id_number[1] = chr(65 + (chr_id - 100) - (26 * (ord(id_number[0]) - 65)))
            id_number = "".join(id_number)
            global df
            for index in range(len(df.columns)):
                if df["ID"].iloc[index] == id_number:
                    id_number = ""
            if id_number != "":
                break

        df1 = pd.DataFrame({"ID":[id_number],
                            "Model":[model],
                            "Buy_Price":[buy_price],
                            "Repair_Cost":[repair_cost],
                            "Realized_Gain":[0],
                            "Profit":[0],
                            "Description":[description]})
        df = pd.concat([df, df1], axis=0)
        print(len(df.columns))
        print(df)
    
    def delete(id_number):
        global df
        for index in range(len(df.columns)):
            if df["ID"].iloc[index] == id_number:
                df = df.drop(index)
        print(df)
Inventory.delete("CJ1309")
Inventory.save()
