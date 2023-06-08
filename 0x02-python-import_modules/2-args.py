#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print(f"{len(argv) - 1} argument", end="")
    if len(argv) == 1:
        print("s.")
    elif len(argv) == 2:
        print(":")
    else:
        print("s:")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
