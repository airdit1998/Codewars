# An ATM ran out of 10 dollar bills and only has 100, 50 and 20 dollar bills.
#
# Given an amount between 40 and 10000 dollars (inclusive)
# and assuming that the ATM wants to use as few bills
# as possible, determinate the minimal number of 100, 50 and 20 dollar
# bills the ATM needs to dispense (in that order)

def withdraw(n):
    result = []
    value = n % 100
    if (value == 10 or value == 30) and n >= 100:
        result.append(int(n // 100) - 1)
    else:
        result.append(int(n // 100))
    n -= result[0] * 100

    if n % 20 == 0:
        result.append(0)
    elif n < 50:
        result.append(0)
    else:
        result.append(1)
    n -= result[1] * 50

    result.append(int(n / 20))
    return result





print(withdraw(1020))