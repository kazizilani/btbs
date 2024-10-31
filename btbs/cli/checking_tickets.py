def Checking_Tickets(User): 
    print("No. \t Bus \t \t Destination")
    for ticket in User["tickets"]:
        print(f"{ticket['ticket-id']} \t {ticket['bus-name']} \t {ticket["from - to"]}")