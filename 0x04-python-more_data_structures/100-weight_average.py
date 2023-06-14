#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weight_score = 0
        weights = 0
        for tup in my_list:
            weight_score += (tup[0] * tup[1])
            weights += tup[1]
        return (weight_score / weights)
    return 0
