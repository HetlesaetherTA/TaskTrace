import sys
sys.path.insert(1, "python")

from file_management import initalize

from colorama import init
from termcolor import colored

init()

OFFLINE_MODE = False
startup_functions = [initalize.checkConnection, initalize.checkSignIn, initalize.checkDirectory, initalize.checkReadWrite]
startup_functions_return_value = ""

for function in startup_functions:
    if OFFLINE_MODE == False: 
        startup_functions_return_value = function()
        bg_color = "on_green"
        if startup_functions_return_value[1] == 1:
            OFFLINE_MODE = True
            bg_color = "on_red"
        print(colored(startup_functions_return_value[0], "white", bg_color))
    else:
        print(colored("ENTERING OFFLINE MODE", "white", bg_color))
        break

