#!/usr/bin/python3
"""Add newlines to a text"""


def text_indentation(text):
    """Prints a text with 2 new lines after: ., ? and :"""

    if type(text) != str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in [':', '.', '?']:
            print(text[i])
            print("")
            if i < len(text) - 1 and text[i + 1] == " ":
                i += 1
        else:
            print(text[i], end="")
        i += 1
