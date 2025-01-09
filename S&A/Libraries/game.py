import random
import sys

def main():
    #get level using check
    n = check("Level: ")
    #get rando number
    rNum = random.randint(1,n)

    #loop guess until it returns false
    while guess(rNum): pass

    #exits when it gets to false
    sys.exit()


def check(message):
    #keep asking for output till wanted awnser
    while True:
        try:
            #makes sure there are no words
            n = int(input(message))
        except ValueError:
            pass
        else:
            #makes sure there are no negatives
            if n > 0: return n

def guess(num):
    #get guess using check
    playerG = check("Guess: ")

    #if number to small
    if playerG < num:
        print("Too small!")
    #if number to big
    elif playerG > num:
        print("Too large!")
    #if number just right
    elif playerG == num:
        print("Just right!")
        #return false to end loop
        return False
    #if it doesnt return false it'll return true
    return True

main()
