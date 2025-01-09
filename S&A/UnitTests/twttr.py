
def main():
    string = input('Input: ')

    print(f'Output: {shorten(string)}')

def shorten(string):
    vowels = {
    'A',
    'E',
    'I',
    'O',
    'U',
    'a',
    'e',
    'i',
    'o',
    'u'
    }


    for v in vowels:
        string = string.replace(v, "")
    return string


if __name__ == "__main__":
    main()






