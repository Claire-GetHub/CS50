
greeting = input('Greeting: ').lower().strip()
amount = 100

if greeting.find('hello') > -1 :
    amount = 0
elif greeting[0] == 'h':
    amount = 20

print(f'${amount}')
