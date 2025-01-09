import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

#make list and get length
command = sys.argv
length = len(command)

#if the length is 1 then there is no commands
if length == 1:
    #set the font to a random font
    figlet.setFont(font= random.choice(figlet.getFonts()))
    #get input then render the text
    print(f"Output: \n {figlet.renderText(input('Input: '))}")
# if the length is 3 and the first comand is correct
elif length == 3 and (command[1] == "-f" or command[1] == "--font"):
    #set the font to the second comand
    figlet.setFont(font= command[2])
    #print the rendered text based on output
    print(f"Output: \n {figlet.renderText(input('Input: '))}")
else:
    #exit if they did something wrong
    sys.exit("Invalid usage")
