#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper = ord(char) - 32
        else:
            upper = ord(char)
        print("{:c}".format(upper), end="")
    print("")
