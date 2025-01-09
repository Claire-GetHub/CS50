
num1, op, num2 = input('Expression: ').split()
num1 = float(num1)
num2 = float(num2)

match op:
    case '-':
        print(num1 - num2)
    case '+':
        print(num1 + num2)
    case '/':
        print(num1 / num2)
    case '*':
        print(num1 * num2)
