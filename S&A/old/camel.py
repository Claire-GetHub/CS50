
string = input('camelCase: ')

for letter in string:
    if letter.isupper():
        print(f'_{letter.lower()}', end= "")
    else:
        print(letter, end="")
print("\n", end="")
