import logging


# def nameCheck(name):
#     if len(name)<2:
#         print("checking if name length ....") # debugging 
#         return "invalid name"
#     elif name.isspace():
#         print("checking if name is space ....")
#         return "invalid name"
#     elif name.isalpha():
#         print("checking if name an alphabet ....")
#         return "invalid name"
#     elif name.replace(' ',' ').isalpha():
#         print("checking for full name ....")
#         return "invalid name"
#     else:
#         print("failed all check")
#         return "name is invalid"
    
# print(nameCheck("AB"))

#using files logging

logging.basicConfig(filename="name.log",level=logging.DEBUG)
#avoid all logings 
logging.disable()
def nameCheck(name):
    if len(name)<2:
        logging.debug("checking if name length ....") # debugging 
        return "invalid name"
    elif name.isspace():
        logging.debug("checking if name is space ....")
        return "invalid name"
    elif name.isalpha():
        logging.debug("checking if name an alphabet ....")
        return "invalid name"
    elif name.replace(' ',' ').isalpha():
        logging.debug("checking for full name ....")
        return "invalid name"
    else:
        logging.debug("failed all check")
        return "name is invalid"
    
print(nameCheck("AB"))