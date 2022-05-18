# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

from collections import Counter


def find_it(seq):
    d = Counter(seq)
    for i in d:
        if d[i] % 2 != 0:
            return i
