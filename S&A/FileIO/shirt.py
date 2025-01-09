#adds a cs50 shirt onto a diffrent image. using the cs50 shirts sizing
#This program wants 2 commandline arguements.
    #1st the name of the image you want the shirt on.
    #2nd where you want the new image saved to

from PIL import Image, ImageOps
import sys

def main():
    #get command arguements
    arg = sys.argv


    #makes sure there are 3 command arguements
        #1st is script,
        #2nd is picture your putting a shirt on,
        #3rd is the name of the new file
    if (len(arg) == 3
    #creates ext which is a list containing extention's returns,
    #extention's parameters are split lists of both command arguements,
    #the if statement uses the 1st parameter (boolean)           ↓
    and (ext := extention(arg[1].split("."), arg[2].split(".")))[0]
    #trys to open image which is either the opened image or the boolean "False"
    and (script := exists(arg[1]))):


        #the actual code
        addShirt(script, arg[2])

    #all the necessary errors
    elif len(arg) > 3:
        sys.exit("Too many command-line arguments ")
    elif len(arg) < 3:
        sys.exit("Too few command-line arguments ")
    #checks what extention's error (the 2nd return) is
    elif ext[1] == "diffrent":
        sys.exit("Input and output have different extensions")
    elif ext[1] == "invalid":
        sys.exit("Invalid input")


def extention(ext1, ext2):
    #parameters
        #ext1 is the extenstion of the first command arguement
        #ext2 is the extenstion of the second command arguement

    #no change to error, then the error is because it was invalid
    error = "invalid"

    #if there is no extention this avoids index error
    ext1 = ext1[1] if len(ext1) > 1 else False
    ext2 = ext2[1] if len(ext2) > 1 else False

    #if its false it returns "invalid" error
    if (ext1 and ext2):
        #if the extentions are diffrent itll return "diffrent" error
        if ext1 == ext2:
            #if it doesnt match it will return "invalid" error
            match ext1:
                case "jpeg" | "jpg" | "png":
                    return True, "correct"
        else:
            error = "diffrent"

    return False, error



#opens the file, returns false if it can't
def exists (fileName):
    try:
        return Image.open(fileName)
    except FileNotFoundError:
        return False


def addShirt (beforeFile, afterName):
    #parameters
        #beforeFile is the opened image, that you want to add the shirt to
    with beforeFile as before:
        #opens the shirt image
        shirt = Image.open("shirt.png")
        size = shirt.size
        #changes the before image size it the shirts size
        before = ImageOps.fit(before, size)
        #pastes the shirt onto the before image.
        #the mask is shirt so the rest of the shirt image stays clear
        Image.Image.paste(before, shirt, mask = shirt)

        #saves the image using the 3rd command arguement as the name
        before.save(afterName)

main()
