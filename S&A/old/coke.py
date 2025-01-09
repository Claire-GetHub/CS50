
due = 50

while due > 0:
    print(f'Amount Due: {due}')
    coins = int(input("Insert Coin: "))
    if coins == 25 or coins == 10 or coins == 5:
        due -= coins
print(f'Change Owed: {abs(due)}')
