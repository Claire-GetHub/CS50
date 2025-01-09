
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    #create total so i can += it
    total = 0
    while True:
        try:
            #checks if its in the dictoinary
            price = menu[input("Item: ").title()]
        except KeyError:
            #try again
            pass
        except EOFError:
            #stop looping
            break
        else:
            #if it is then add it to the price
            total += price
            print(f"Total: ${total:.2f}")


main()
