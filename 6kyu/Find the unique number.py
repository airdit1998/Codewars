from collections import Counter


def find_uniq(arr):
    for i, k in Counter(arr).items():
        if k == 1:
            return i


a = [1, 1, 3, 3, 1, 2, 1, 1]
find_uniq(a)
