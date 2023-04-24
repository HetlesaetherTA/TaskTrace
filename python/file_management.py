from utility import Animations
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
        Animations.start(Animations.spinner, "Checking Connection ")
        try:
            # ping3 will print text not return it. Disabling print to output is not visable to user.
            text_trap = io.StringIO()
            sys.stdout = text_trap
            ping3.verbose_ping("www.apple.com")
            sys.stdout = sys.__stdout__
            Animations.kill() 
            return ("Apple.com - OK", 0)
        except Exception as e:
            sys.stdout = sys.__stdout__
            Animations.kill()
            print(e)
            return ("Fail to ping apple.com, check if you're connected to internet", 1)

    def checkSignIn(): 
        print(sys.path)
        try: 
            username = "hetlesaetherspam@gmail.com"
            pw = open(sys.path[0], "r")
            password = pw.read() 
            pw.close() 

            global api 
            api = PyiCloudService(username, password) 
            api.params['clientID'] = api.client_id 
            api.drive.params["clientId"] = api.client_id 
            Animations.kill() 
            return ("Sign In - OK", 0) 
        except Exception as e: 
            print(e)
            Animations.kill()
            return ("Failed to sign into your iCloud account, check if you're using valid credentials", 1)
    
    def checkDirectory(): 
        Animations.start(Animations.spinner, "Checking Directory ")
        if "TaskTrace" not in api.drive.dir():
            Animations.kill()
            Animations.start(Animations.spinner, "Creating Directory ")
            response = api.drive.mkdir('TaskTrace')
            if response['folders'][0]['status'] != "OK":
                Animations.kill()
                return ("Filed to initialize directory - Send in an issue on github", 1)
            Animations.kill()
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
