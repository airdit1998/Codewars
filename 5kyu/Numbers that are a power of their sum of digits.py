def find_degree(digit, digit_sum):
    for degree in range(10):
        if digit_sum ** degree == digit:
            return digit
        else:
            continue


def power_sumDigTerm(n):
    i = 80
    digits = []
    while True:
        i1 = list(map(int, str(i)))
        digit_sum = sum(i1)
        if find_degree(digit=i, digit_sum=digit_sum):
            digits.append(i)
        i += 1
        if len(digits) == n:
            break

    return digits[n - 1]
