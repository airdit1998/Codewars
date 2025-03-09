# Given two arrays a and b write a function comp(a, b)
# that checks whether the two arrays have the "same" elements,
# with the same multiplicities. "Same" means, here,
# that the elements in b are the elements in a squared, regardless of the order.


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    array1.sort(key=abs)
    array2.sort(key=abs)
    return all(a ** 2 == b for a, b in zip(array1, array2))