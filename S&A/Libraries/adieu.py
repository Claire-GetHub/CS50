import inflect

def main():
    #the needed thing to join pieces
    p = inflect.engine()
    #print the sentence start then get list from function then join them
    print(f"Adieu, adieu, to {p.join(getList())}")


def getList():
    #create empty list
    names = []
    #keep getting names until it they enter nothing
    while True:
        try:
            #get the name
            item = input("Name: ")
        except EOFError:
            #if no more names return
            return names
        else:
            #add that name to the list
            names.append(item)


main()
