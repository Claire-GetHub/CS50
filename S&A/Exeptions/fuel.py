
def main():
    X, Y = getInts()
    #testing -->> print(f"X: {X}\nY: {Y}")

    #making sure y isn't 0 and X is less than one
    if (X <= Y) and not(Y == 0):
        #get the percentage
        percentage = (X/Y)
        if percentage <= .1:
            #less than on its empty
            print("E")
        elif percentage >= .99:
            #greater than 99 its full
            print("F")
        else:
            #anything else it prints the percentage
            print(f'{percentage:.0%}')
    else:
        #if its not less than or y == 0 then run again
        main()

def getInts():
    while True:
        #gets input and splits it
        str = input("Fraction: ").strip().split("/"))
        try:
            #if both are numbers return it
            return int(str[0]), int(str[1])
        except ValueError:
            #if not try again
            pass
main()
