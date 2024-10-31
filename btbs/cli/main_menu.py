from sys import exit
from lib.utils import Request, Error

def Main_Menu():
    print("=== Main Menu ===")
    print("1. Login")
    print("2. Exit")

    req = Request()

    isValid = False

    while not isValid:
        if(req == str(1) or req == str(2)):
            isValid = True
            return req

        else:
            isValid = False
            req = Error()
        
        

