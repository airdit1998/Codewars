# It's 9 time!
# I want to count from 1 to n. How many times will I use a '9'?
from time import time
import numpy as np
from time import time
from collections import Counter

def count_nines(n):
    if n < 100000000:
        i = 0
        for num in range(1, n + 1):
            if '9' in str(num):
                nine_count = len([x for x in list(str(num)) if x == '9'])
                i += nine_count
            else:
                pass
        return i
    else:
        return 0


a = time()
#print(count_nines(10000000))
print(count_nines(11040252174950481636))
print(time() - a)