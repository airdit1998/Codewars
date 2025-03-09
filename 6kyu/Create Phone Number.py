# Write a function that accepts an array of 10 integers
# (between 0 and 9), that returns a string of those
# numbers in the form of a phone number.

def create_phone_number(n):
    a = '(' + ''.join(str(e) for e in n[:3]) + ')'
    b = ''.join(str(i) for i in n[3:6])
    c = ''.join(str(i) for i in n[6:])
    return a + ' ' + b + '-' + c


# sample
def create_phone_number_second(n):
    n = ''.join(map(str, n))
    print(n)
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
