

def main():
    dict = {}
    while True:
        try:
            item = input()
        #grab an input until they do ctrl D
        except EOFError:
            #alphabetitize dictionary

            #get the keys and make the into a list
            keys = list(dict.keys())
            #sort the list
            keys.sort()
            #create new dictionary by doing key = dict[key] for as many keys there are
            dict = {i: dict[i] for i in keys}
            #print out everything
            for item in dict:
                print(f"{dict[item]} {item.upper()}")
            break
        else:
            #if the item is already in dict add one to the value
            if item in dict:
                dict[item] += 1
            else:
                #otherwise create the key and make it 1
                dict[item] = 1


main()
