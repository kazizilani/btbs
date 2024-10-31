from random import randint

def Book_Ticket(selected_bus, selected_from, selected_to):
    new_ticket = {
            "ticket-id": randint(0,100),
            "bus-name": selected_bus,
            "from - to": f"{selected_from} : : {selected_to}"
        }
    print("Ticket Booked!")
    return new_ticket
    
    