
def Request(msg=None):
   if(msg):
      return str(input(f"{msg}: "))
   else:
      return str(input("Please Enter An Option: "))


def Error():
   return str(input("Please Enter A Valid Option: "))
