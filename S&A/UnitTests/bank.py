
def main():
    greeting = input('Greeting: ').lower().strip()
    amount = value(amount)
    print(f'${amount}')

def value(greeting):
    greeting = greeting.lower()
    if greeting.find('hello') > -1 :
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()






