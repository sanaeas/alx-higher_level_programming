#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(argv) - 1} argument:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
