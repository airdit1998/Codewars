# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

def solve(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]
