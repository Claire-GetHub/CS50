
def main():

    while True:
        try:
            percentage = convert("Fraction: ")
        except(ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(percentage))
            break







def convert(fraction):
    str = fraction.strip().split("/")
    X, Y = str[0], str[1]
    if X.isdigit() and Y.isdigit():
        X, Y = int(X), int(Y)
        if not(Y == 0):
            if (X <= Y):
                return int((X/Y) * 100)
            else:
                raise ValueError
        else:
            raise ZeroDivisionError
    raise ValueError

def gauge(percentage):
    if percentage <= 1:
        #less than on its empty
        return "E"
    elif percentage >= 99:
        #greater than 99 its full
        return "F"
    else:
        #anything else it prints the percentage
        return f'{percentage}%'

if __name__ == "__main__":
    main()
