# Create a function named rotate() that accepts a string argument
# and returns an array of strings with each letter
# from the input string being rotated to the end.

def rotate(str_):
    arr = []
    n = range(1, len(str_) + 1)
    for i in n:
        arr.append(str_[i:] + str_[:i])
    return arr