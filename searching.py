import random
import math
import os
from sorting import *


# Sequential search returns the value and index
def linear_search(sequence, target):
    for i, v in enumerate(sequence):
        if v == target:
            return i
    return 'The target could not be found'


# Binary search
# Need to revisit to figure out how to return index
def binary_search(sequence, target):
    # Sort the list ascending
    sequence = sequence.copy()
    sequence = selection_sort(sequence)
    if 'iteration' not in locals():
        iteration = 0
    half = len(sequence) // 2
    while bool(half):  # True when > 0
        iteration += 1
        if target == sequence[half]:
            return 'Found in ' + str(iteration) + ' iterations.'
        elif target > sequence[half]:
            return binary_search(sequence[half:], target)
        else:
            return binary_search(sequence[:half], target)
    return 'The target could not be found'


def jump_search(sequence, target):
    sequence = selection_sort(sequence.copy())
    jump = round(math.sqrt(len(sequence)))
    slices = [i * jump for i in range(len(sequence) // jump)]  # jump indices
    for i, v in enumerate(slices):
        if sequence[v] == target:
            return 'The target was found'
        elif v != slices[-1]:  # when not on last item; avoids index err
            if sequence[slices[i + 1]] > target:
                return linear_search(sequence[v:slices[i + 1]], target)
        else:
            return linear_search(sequence[v:], target)


if __name__ == "__main__":
    # seq = [random.randint(0, 256) for i in range(20)]
    seq = [6, 7, 8, 1, 2, 3, 4, 5]

    print("Linear Search:\n" + str(linear_search(seq, 6)))  # True
    print(str(linear_search(seq, 69)) + "\n")  # False

    print("Binary Search:\n" + binary_search(seq, 2))  # True
    print(binary_search(seq, 2))  # True
    print(binary_search(seq, 69) + "\n")  # False

    print("Jump Search:\n" + str(jump_search(seq, 6)))  # True
    print(str(jump_search(seq, 69)) + "\n")  # False
