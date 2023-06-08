#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    def_names = dir(hidden_4)
    for name in def_names:
        if name[0] == "_" and name[1] == "_":
            continue
        print(name)
