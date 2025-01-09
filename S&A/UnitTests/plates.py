def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def afterNum (s):
    for c in s:
        if not(c.isalpha()):
            if c == '0':
                return False
            else:
                after = s.index(c)
                break
    else:
        return True

    for n in range(after, len(s)):
        if s[n].isalpha():
            return False
    else:
        return True

def punctuation (s):
    for c in s:
        if not(c.isalpha() or c.isdigit()):
            return False
    else:
        return True

def is_valid(s):
    if (s[0:1].isalpha()) and (len(s) >= 2 and len(s) <= 6) and afterNum(s) and punctuation(s):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
