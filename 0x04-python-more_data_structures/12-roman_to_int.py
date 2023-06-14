#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (isinstance(roman_string, str) is False):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string) - 1):
        if roman[roman_string[i]] < roman[roman_string[(i+1)]]:
            result -= roman[roman_string[i]]
        else:
            result += roman[roman_string[i]]
    return result + roman[roman_string[-1]]
