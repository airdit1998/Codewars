# Create a function that takes 2 nonnegative integers in
# form of a string as an input, and outputs the sum (also as a string):

def sum_str(a, b):
    if a != "" and b != "":
        return str(int(a) + int(b))
    elif a == "" and b == "":
        return '0'
    elif a == "":
        return b
    else:
        return a


print(sum_str("9", ""))