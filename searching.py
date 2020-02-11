import random
import math
import os

seq = [random.randint(0, 256) for i in range(20)]


# Sequential search returns the value and index
def sequential_search(sequence, target):
    found = False
    for i, v in enumerate(sequence):
        if v == target:
            return v, i
    if not found:
        print("The target could not be found")


def sort_iterator(sequence, reverse=False):
    sort = []
    length = len(sequence)
    while len(sort) < length:
        if not reverse:
            res = [math.inf, 0]
        else:
            res = [-math.inf, 0]
        for i, v in enumerate(sequence):
            if not reverse:
                if v <= res[0]:
                    res = [v, i]
            else:
                if v >= res[0]:
                    res = [v, i]
        sort.append(sequence.pop(res[1]))
    return sort


# Binary search
def binary_search(sequence, target):
    # Sort the list ascending
    half = len(sequence) // 2
    while half > 0:
        sequence = sort_iterator(sequence)
        if target == sequence[half]:
            return True
        elif target > sequence[half]:
            return binary_search(sequence[half:], target)
        else:
            return binary_search(sequence[:half], target)
    return False


binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8)
