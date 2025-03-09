# Given two arrays of strings, return the number of times
# each string of the second array appears in the first array.


def solve(a, b):
    return [a.count(i) if i in a else 0 for i in b]
