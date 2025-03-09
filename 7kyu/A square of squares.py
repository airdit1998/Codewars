# Given an integral number,
# determine if it's a square number:
import math


def is_square(n):
    if n >= 0:
        return math.sqrt(n).is_integer()
    else:
        return False
