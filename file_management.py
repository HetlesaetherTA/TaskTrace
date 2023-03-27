from pyicloud import PyiCloudService
from time import sleep
import ping3

try:
    ping.verbose_ping("www.apple.com", count=3)
except:
    print("Fail to ping apple.com, check if you're connected to internet")

# username = "hetlesaetherspam@gmail.com"
# pw = open("password.txt", "r")
# password = pw.read()
# pw.close()

# api = PyiCloudService(username, password)

# api.params['clientID'] = api.client_id
# api.drive.params["clientId"] = api.client_id

# if "TaskTrace" not in api.drive.dir():
#     response = api.drive.mkdir('TaskTrace')
#     if response['folders'][0]['status'] != "OK":
#         raise Exception("Not able to create TaskTrace folder in root")
