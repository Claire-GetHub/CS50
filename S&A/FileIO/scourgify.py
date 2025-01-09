import csv
import sys


def main():
    #get command arguements
    arg = sys.argv
    #makes sure there is a command arguement, checks if the file exists, and if its a csv file
    if len(arg) == 3  and (check := (arg[1].split(".")[1] == "csv")) and (script := exists(arg[1])):
        rewrite(script, arg[2])

    #all the necessary errors
    elif len(arg) > 3:
        sys.exit("Too many command-line arguments ")
    elif len(arg) < 3:
        sys.exit("Too few command-line arguments ")
    elif script == False and check:
        sys.exit(f"Could not read {script}")
    else:
        sys.exit("Not a CSV file")

#opens the file, returns false if it can't
def exists (fileName):
    try:
        return open(fileName, "r")
    except FileNotFoundError:
        return False

def rewrite (beforeFile, afterName):
    #opens the old and new file
    with beforeFile as before, open(afterName, "w") as after:
        #makes it dict readable
        reader = csv.DictReader(before)
        #makes it dict writable
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])

        #writes the heading
        writer.writeheader()
        for row in reader:
            #splits first and last name
            last, first = row["name"].split(", ")
            #writes down each row
            writer.writerow({'first': first, 'last': last, 'house': row["house"]})

main()

