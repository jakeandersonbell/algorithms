import math


def selection_sort(sequence, reverse=False):
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