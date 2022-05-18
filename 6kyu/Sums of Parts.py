# Let us consider this example (array written in general format):
# ls = [0, 1, 3, 6, 10]
#
# Its following parts:
# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []

# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
# The function parts_sums (or its variants in other languages)
# will take as parameter a list ls and return a list of the sums of its parts as defined above.

def parts_sums(ls):
    sum_list = []
    if len(ls) == 0:
        return [0]
    else:
        while len(ls) != 0:
            s = sum(ls)
            sum_list.append(s)
            ls.pop(0)
        sum_list.append(0)
        return sum_list

def parts_sums(ls):
    sums = [0] * (len(ls) + 1)
    for i, e in enumerate(reversed(ls)):
        sums[len(ls) - i - 1] += sums[len(ls) - i] + e
    return sums