from db.busses import Busses
from lib.cds import Stack
from lib.utils import Request, Error

def Choose_Bus(selected_from, selected_to):
    #?creates stack and checks all routes of a bus, if any bus goes from the source to destiantion it adds that to the stack
    avaialble_busses = Stack()

    for Bus in Busses:
        for route in Bus["bus-routes"]:
            if route == selected_from:
                for r in Bus["bus-routes"]:
                    if(r == selected_to):
                        avaialble_busses.push(Bus)
                        break
    
    #?ensure that at least one bus goes from source to destination
    if len(avaialble_busses.stack) > 0:
        print("Bus No. \t Bus Name \t Empty \t Fare")
        for bus in avaialble_busses.stack:
            print(f"{bus['bus-id']} \t {bus['bus-name']} \t {bus["available-seats"]} \t {bus['fare']}")
    
    #?otherwise writes sorr       
    else:
        print("Sorry, No Bus In This Rotue")
    
   
    #?input bus id, and keep prompting as long as the input is not an availbe bus
    selected_bus_id = Request("Enter Bus No.")
    
    #? detach the availbe bus id, and checks that input bus id is a availbe and prompts until its right
    avaialble_busses_id = Stack()
    for bus in avaialble_busses.stack:
        avaialble_busses_id.push(bus["bus-id"])

    #?checks id with user input and return the bus name if matched
    for Bus in Busses:
        if(str(Bus["bus-id"]) == selected_bus_id):
            print(Bus["bus-name"])
            return [Bus["bus-name"], Bus["available-seats"]]
