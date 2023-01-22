# Write a function that takes a string of parentheses,
# 0.
# and determines if the order of the parentheses is valid.
# The function should return true if the s2tring is valid, and false if it's invalid.

def valid_parentheses(string):
    valid=[]
    for s in string:
        if s == "(":
            valid.append(s)
        elif s == ")":
            try:
                valid.pop()
            except:
                return False
    if len(valid) == 0:
        return True
    else:
        return False
