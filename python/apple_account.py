from pyicloud import PyiCloudService
import getpass
import os

USERNAME_FROM_FILE = False

class Account():
    def login():
        try:
            try:
                username_file = open("username.txt", "r")
                global username
                username = username_file.read()
                username_file.close()
               
                if username != "NO USERNAME":
                    global USERNAME_FROM_FILE
                    USERNAME_FROM_FILE = True
            except Exception as e:
                USERNAME_FROM_FILE = "pending"
                print(e)
            
            if USERNAME_FROM_FILE != True:
                username = input("email: ")
            password = getpass.getpass("password: ")

            global api 
            api = PyiCloudService(username, password) 
            api.params['clientID'] = api.client_id 
            api.drive.params["clientId"] = api.client_id 
            print(USERNAME_FROM_FILE)
            if isinstance(USERNAME_FROM_FILE, str):
                save_email = input("Do you wish to save your email? (y | n):")

            try:
                if isinstance(USERNAME_FROM_FILE, str):
                    username_file = open("username.txt", "w")
                if save_email.upper() == "Y":
                    username_file.write(username)
                    username_file.close()
                elif save_email.upper() == "N":
                    username_file.write("NO USERNAME")
                else:
                    username_file.close()
                    os.remove("username.txt")
                    raise Exception("No save")
            except: 
                print("No changes made")
            return ("Sign In - OK", 0) 
        except Exception as e:
            print(e)
            return ("Failed to sign into your iCloud account, check if you're using valid credentials", 1)
        
print(Account.login())
