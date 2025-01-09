def main():
    time = input().split(':')[0]
    time = int(time)
    print(convert(time))

def convert(time):
    if time <= 10 and time >= 5:
        return 'breakfast time'
    elif time >= 12 and time <= 17:
        return 'lunch time'
    elif time < 17:
        return 'dinner time'

if __name__ == "__main__":
    main()
