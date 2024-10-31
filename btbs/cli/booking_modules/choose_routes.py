from db import cities
from lib.utils import Request, Error
Cities = cities.Cities

def Choose_Routes():
    
    for i,city in enumerate(Cities):
        print(f"{i}. {city}")


    #?getting input for From and keep prompting users until we get a valid destination
    selected_from = Request("From") 

    while selected_from > str(len(Cities)) or selected_from < str(0):
        selected_from = Request("From")



    #? same thing but for To
    selected_to = Request("To")

    while selected_to > str(len(Cities)) or selected_to < str(0):
        selected_to = Request("To")

    while selected_to == selected_from:
        selected_to = Request("Please Enter A Different To")

    return {"selected_from": Cities[int(selected_from)], "selected_to": Cities[int(selected_to)]}
