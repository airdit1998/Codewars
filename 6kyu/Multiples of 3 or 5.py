# Finish the solution so that it returns the
# sum of all the multiples of 3 or 5 below the number passed in.

def solution(number):
    i = 0
    if number < 0:
        return 0
    else:
        for d in range(0, number):
            if d % 3 == 0 or d % 5 == 0:
                i += d
        return i


def solution_1(number):
    return sum([x for x in range(0, number) if x % 3 == 0 or x % 5 == 0])