# Consider an array/list of sheep where some sheep may be missing
# from their place. We need a function that counts the number
# of sheep present in the array (true means present).


def count_sheeps(sheep):
    return len([x for x in sheep if x is True])
