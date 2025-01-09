def main():
    time = convert(input('What time is it? '))
    if time <= 10 and time >= 5:
        print('breakfast time')
    elif time >= 12 and time <= 17:
        print('lunch time')
    elif time >= 17:
        print('dinner time')

def convert(time):
    time = time.split(':')
    hour = int(time[0])
    min = int(time[1])/60
    return hour + min



if __name__ == "__main__":
    main()
