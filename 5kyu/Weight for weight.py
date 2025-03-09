def order_weight(strng):
    d = {}
    for digit in strng.split(' '):
        print(digit)
        d[digit] = sum([int(x) for x in digit])
    print(d)
