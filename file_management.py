from pyicloud import PyiCloudService
from shutil import copyfileobj
from importlib import reload
from time import sleep
import ping3
import io
import os
import sys

ping3.EXCEPTIONS = True

#TODO 

#add log files insted of printing minor errors
# error: checkReadWrite will sometimes not clean TaskTrace folder after running
class initalize:
    def checkConnection():
        try:
            # ping3 will print text not return it. Disabling print to output is not visable to user.
            text_trap = io.StringIO()
            sys.stdout = text_trap
            ping3.verbose_ping("www.apple.com")
            sys.stdout = sys.__stdout__
            
            return ("Apple.com - OK", 0)
        except:
            sys.stdout = sys.__stdout__
            return ("Fail to ping apple.com, check if you're connected to internet", 1)

    def checkSignIn():
        try:
            username = "hetlesaetherspam@gmail.com"
            pw = open("password.txt", "r")
            password = pw.read()
            pw.close()
            
            global api
            api = PyiCloudService(username, password)

            api.params['clientID'] = api.client_id
            api.drive.params["clientId"] = api.client_id
            return ("Sign In - OK", 0)
        except:
            return ("Failed to sign into your iCloud account, check if you're using valid credentials", 1)
    
    def checkDirectory(): 
        if "TaskTrace" not in api.drive.dir():
            response = api.drive.mkdir('TaskTrace')
            if response['folders'][0]['status'] != "OK":
                return ("Filed to initialize directory - Send in an issue on github", 1)
        return ("Directory - OK", 0)
    def checkReadWrite():
        # Might be an error library. It needs to be reloaded for new files/folders to be recognized.
        from pyicloud import PyiCloudService
        initalize.checkSignIn()

        f = open("test.txt", 'w')
        f.write("a")
        f.close()
        
        try:
            with open("test.txt", 'rb') as f:
                api.drive['TaskTrace'].upload(f)
                return ("Read/Write - OK", 0)
        except:
            return ("Failed to write to iCloud", 1)
        try:
            testfile = api.drive['TaskTrace']['test.txt']  
            with testfile.open(stream=True) as response:
                with open("testreturn.txt", 'wb') as file_out:
                    copyfileobj(response.raw, file_out)
            if open("testreturn.txt", 'r').read() != 'a':
                raise Exception("error")
        except: 
            return ("Failed to read from iCloud", 1)
        try:
            api.drive['TaskTrace']['test.txt'].delete()
        except:
            return ("Failed to delete from iCloud", 1)
        
        if os.path.exists("test.txt"):
            os.remove("test.txt")
        else:
            print("Minor Warning - unable to find and delete local test file")
        if os.path.exists("testreturn.txt"):
            os.remove("testreturn.txt")
        else:
            print("Minor Warning - unable to find and delete local test file")
        return ("Read/Write - OK", 0)


