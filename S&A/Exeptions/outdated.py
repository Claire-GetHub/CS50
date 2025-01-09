import re

#used to check if its a month and to give the month a number
monthNum = {'jan': 1,'feb': 2,'mar': 3,'apr': 4,'may': 5,'jun': 6,'jul': 7,'aug': 8,'sep': 9,'oct': 10,'nov': 11,'dec': 12}


def main():
    month, day, year = check()
    #print
    print(f"{year}-{month:02}-{day:02}")

def check():
    while True:
        #get the input so i can check if it has / or ,
        statement = re.sub(' +', ' ',input("Date: ").strip())
        #splits it so stuff is usable
        date = re.split(' / |/ | /|/| , | ,|, |,| ', statement)
        try:
            #for month, returns the cut down version of the word if there are no "/" and there is a ",". otherwise it just returns the integer version of date if the int is < 12
            #for day, turns the second input into a number if its less than 31, otherwise it makes it a string so the function will return an error
            #for year, it turns it into a month
            return monthNum[(date[0]).lower()[0:3]] if statement.find("/") == -1 and statement.find(",") > 0 elif (num := int(date[0])) < 12 num, \
            int((day := date[1]) if len(day) <= 2 and int(day]) < 31 else "notDay"), \
            int(date[2])
        except KeyError or ValueError:
            pass


main()
