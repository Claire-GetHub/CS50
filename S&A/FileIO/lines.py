import sys

def main():
    #get command arguements
    arg = sys.argv

    #makes sure there is a command arguement, checks if the file exists, and if its a python file
    if len(arg) == 2 and (script := exists(arg[1])) and (pyCheck := arg[1].split(".")[1] == "py"):
        #gets amount of lines
        lines = lineAmount(script)
        print(lines)
    #all the necessary errors
    elif len(arg) > 2:
        sys.exit("Too many command-line arguments ")
    elif len(arg) < 2:
        sys.exit("Too few command-line arguments ")
    elif script == False and pyCheck:
        sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

#opens the file, returns false if it can't
def exists (fileName):
    try:
        return open(fileName, "r")
    except FileNotFoundError:
        return False

#counts lines
def lineAmount (script):
    amount = 0
    #for all lines in script
    for line in script:
        #remove the new line
        line = line.strip().strip("\n")
        #if its not a comment and there is stuff on the string
        if not(line.startswith("#")) and line:
            #adds a line
            amount += 1
    #returns the amount of lines
    return amount

main()

