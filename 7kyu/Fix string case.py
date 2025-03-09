# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters
# and your task is to convert that string to either lowercase only or uppercase only based on:


def solve(s):
    return ''.join([s.lower() if len([x for x in s if x.islower()]) >= len(s) / 2 else s.upper()])
