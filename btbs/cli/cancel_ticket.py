from cli.checking_tickets import Checking_Tickets
import lib.utils 
from lib.cds import Stack


def Cancel_Ticket(User):
    Checking_Tickets(User)
    selected_option = lib.utils.Request("Enter Ticket No.")
    
    available_tickets = []

    for ticket in User["tickets"]:
        available_tickets.append(str(ticket["ticket-id"]))
    
    while selected_option not in available_tickets:
        selected_option = lib.utils.Error()
    
    for i, ticket in enumerate(User["tickets"]):
        if ticket["ticket-id"] == int(selected_option):
            User["tickets"].pop(i)
            print(f"Ticket No. {ticket["ticket-id"]} Cancelled")
            Checking_Tickets(User)
    return User

    