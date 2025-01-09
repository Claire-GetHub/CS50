import random

def main():
    #get level using get_level()
    level = get_level()
    #initialize score to display at the end
    score = 0

    #go for 10 times
    for i in range(10):
        #generate first num
        X = generate_integer(level)
        #generate second num
        Y = generate_integer(level)

        #check returns true or false
        if check(X,Y):
            #add score since true means the anwser is correct
            score += 1
        else:
            #show anwser because false means they got it wrong 3 times
            print(f"{X} + {Y} = {X + Y}")
    #print score
    print(f"Score: {score}")

def check(X, Y):
    #only 3 tries
    for _ in range(3):
            try:
                #makes sure there are no words
                n = int(input(f"{X} + {Y} = "))
            except ValueError:
                pass
            else:
                if n == (X + Y):
                    #returns true if they got it right
                    return True
                else:
                    #prints EEE if they got it wrong
                    print("EEE")
    #returns false after all 3 tries are used
    return False

def get_level():
    while True:
        try:
            #makes sure level is a number
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            #makes sure level is 1 - 3
            if n > 0 and n < 4:
                #returns n if its an allowed level
                return n


def generate_integer(level):
    #if its level 1, numbers are 0 - 9
    if level == 1:
        return random.randint(0,9)
    #if its level 2, numbers are 10 - 99
    elif level == 2:
        return random.randint(10,99)
    #if its level 3, numbers are 100 - 999
    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
