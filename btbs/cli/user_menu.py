from lib.utils import Request, Error

def User_Menu():
    print("=== User Menu ===")
    print("1. Book A Ticket")
    print("2. Check All Tickets")
    print("3. Cancel A Ticket")
    print("4. Logout")
    
    

    isValid = False
    
    while not isValid:
        req = Request()
        if(req  < str(5) or req > str(0)):
            isValid = True
            return req
        else: continue

        

