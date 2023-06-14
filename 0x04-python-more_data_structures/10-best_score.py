#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    best = max(list(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if value == best:
            return key
