import requests
import sys

def main():
    #get amount placed in command line
    amount = commandCheck()
    #get the current rate
    rate = rateUSD()
    #print amount * rate with 4 decimals and commmas
    print(f"${amount * rate:,.4f}")


def rateUSD():
    #makes sure you get the requested file
    while True:
        try: 
            #request the json using the provided link
            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            #go through all the nested dictionaries and get the value I want
            return r.json()["bpi"]["USD"]["rate_float"]
        #if theyres a problem try again
        except requests.RequestException:
            pass

def commandCheck():
    #get the command arguemnets
    cInput = sys.argv
    #makes sure there is a agruement of use
    if len(cInput) == 2:
        try:
            #try to turn it into a float
            return float(cInput[1])
        except ValueError:
          #if i cant exit with an error
          sys.exit("Command-line argument is not a number ")
    else:
        #if there is no agruement of use exit with an error
        sys.exit("Missing command-line argument ")


main()
