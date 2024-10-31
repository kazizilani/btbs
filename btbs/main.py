#import from database folder
from db import users, cities, busses

#storing the data for read/write operaton
Users = users.Users
Cities = cities.Cities
Busses = busses.Busses


#login related information
logged_in = False
user_id = -1

#import interface modules
from cli import main_menu, login, user_menu, checking_tickets, cancel_ticket, booking

#import methods from library 
from lib import utils

while True:
    if not logged_in:
        option_selected = main_menu.Main_Menu()

        if(option_selected == str(1)):
            user_id = login.Login(Users)
            if(user_id > -1):
                logged_in = True
    
        else:
            break

    else:
        #? setting current user to verified user
        User = Users[user_id]
        option_selected = 0
        while option_selected != 4:
            #? taking input from user menu
            option_selected = int(user_menu.User_Menu())

            if option_selected == 1:
        #?books new ticket and return modified user
                User = booking.Booking(User)
        
        #?displays all the ticket
            elif option_selected == 2:
                checking_tickets.Checking_Tickets(User)
        
        #? cancels a ticket and modider user
            elif option_selected == 3:
                User = cancel_ticket.Cancel_Ticket(User)
        
        #? loggin out & showing main menu
            elif(option_selected == 4):
                logged_in = False
                user_id = -1
            else:
                utils.Error()
            

    """
                 
            
        if request == 1:
            Booking(user_index, User)
        elif request == 2:
            Checking_Tickets(User)
        elif request == 3:
           User = Cancel_Ticket(user_index, User)
        elif request==4:
            return 4
        else:
            Error()
          
                    
    """
