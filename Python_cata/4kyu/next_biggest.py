def check_biggest(digit):
    digit_list = sorted([int(x) for x in list(str(digit))], reverse=True)
    return int(''.join([str(x) for x in digit_list]))


def find_next_digit(digit):
    old_digit = sorted(str(digit))
    while True:
        digit += 1
        if old_digit == sorted(str(digit)):
            return digit


def next_bigger(n):
    if check_biggest(n) == n:
        return -1
    else:
        return find_next_digit(n)
