import random
import math
import os


# Sequential search returns the value and index
def linear_search(sequence, target, addition=False):
    found = False
    for i, v in enumerate(sequence):
        if v == target:
            res = "The target was found"
            if addition:
                pass
                # res = res + " in addition"
            return res
    if not found:
        return "The target could not be found"


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
# Need to revisit to figure out how to return index
def binary_search(sequence, target):
    # Sort the list ascending
    sequence = sequence.copy()
    sequence = sort_iterator(sequence)
    if 'iteration' not in locals():
        iteration = 0
    half = len(sequence) // 2
    while bool(half):
        iteration += 1
        if target == sequence[half]:
            return 'Found in ' + str(iteration) + ' iterations.'
        elif target > sequence[half]:
            return binary_search(sequence[half:], target)
        else:
            return binary_search(sequence[:half], target)
    return 'The target could not be found'


def jump_search(sequence, target):
    sequence = sort_iterator(sequence.copy())
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
    seq = [1, 2, 3, 4, 5, 6, 7, 8]

    print("Linear Search:\n" + linear_search(seq, 6))  # True
    print(linear_search(seq, 69) + "\n")  # False

    print("Binary Search:\n" + binary_search(seq, 2))  # True
    print(binary_search(seq, 2))  # True
    print(binary_search(seq, 69) + "\n")  # False

    print("Jump Search:\n" + jump_search(seq, 6))  # True
    print(jump_search(seq, 69) + "\n")  # False
