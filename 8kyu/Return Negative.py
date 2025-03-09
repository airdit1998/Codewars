# In this simple assignment you are given a number
# and have to make it negative. But maybe the number is already negative?

def make_negative(number):
    return number * -1 if number >= 0 else number
