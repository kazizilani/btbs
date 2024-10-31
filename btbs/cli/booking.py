from cli.booking_modules import choose_routes, choose_bus, book_ticket
from lib.cds import Queue
def Booking(User):
    queue = Queue()    
    #?show and take imput for from & to and return from and to in dictionary form
    Routes = choose_routes.Choose_Routes()

    #?deconstruct Routes and get the from & to
    selected_from = Routes["selected_from"]
    selected_to = Routes["selected_to"]

    #? pass from & to, and get the choosen bus name & seats availabe
    selected_bus_info = choose_bus.Choose_Bus(selected_from, selected_to)
    selected_bus = selected_bus_info[0]
    selected_bus_seats = selected_bus_info[1]
    booked_ticket = book_ticket.Book_Ticket(selected_bus, selected_from, selected_to)
    if selected_bus_seats < 1:
        print("Ticket In Queue")
        queue.enqueue(booked_ticket)    
    else:
        User["tickets"].append(booked_ticket)
    return User

