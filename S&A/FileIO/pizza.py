from tabulate import tabulate
import csv
import sys

def main():
    #get command arguements
    arg = sys.argv
    #makes sure there is a command arguement, checks if the file exists, and if its a csv file
    if len(arg) == 2  and (check := (arg[1].split(".")[1] == "csv")) and (script := exists(arg[1])):
        print(printMenu(script))

    #all the necessary errors
    elif len(arg) > 2:
        sys.exit("Too many command-line arguments ")
    elif len(arg) < 2:
        sys.exit("Too few command-line arguments ")
    elif script == False and check:
        sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")

#opens the file, returns false if it can't
def exists (fileName):
    try:
        return open(fileName, "r")
    except FileNotFoundError:
        return False

def printMenu(pizzaFile):
    with pizzaFile as csvfile:
        #turns file into iterable
        reader = csv.DictReader(csvfile)
        list = []
        #iterates
        for row in reader:
            #turns the keys into a list so it can become the header
            headers = [*(row.keys())]

            #uses the header to add each value into a list then appends that list
            list.append([row[headers[0]],row[headers[1]],row[headers[2]]])

        #returns the menu
        return tabulate(list, headers, tablefmt="grid")

main()





table = {
    "cat":7
}

print(table["cat"])
