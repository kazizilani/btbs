import lib.utils

def Login(Users):
    """
    ? user index: user postion in array
    ? user_exists: checks if users exists
    ? password: checks if the password is correct
    """
    user_index = -1
    user_exists = correct_password = False

    print("'\n# Main Menu")



    while not user_exists:
        username = lib.utils.Request("Enter Your Username")

        #?return to main menu
        if username == "#":
            return -1

        for i, User in enumerate(Users):
            if(User["username"]) == username:
                user_index = i
                user_exists = True
            else: continue
        if (not user_exists):
            print("No User Exists")
        else:
            while not correct_password:
                password = lib.utils.Request("Enter Password")
                if Users[user_index]["password"] == password:
                    correct_password = True
                    print(f"Welcome! {Users[user_index]["username"]}\n")
                    
                    return user_index
                else:
                    print("Wrong Password")




             

          

        