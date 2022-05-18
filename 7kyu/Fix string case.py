def solve(s):
    if s.isupper():
        return 1
    elif s.islower():
        return 2
    # elif [x.upper().count(x) for x in s] == [x.lower().count(x) for x in s]:
    #     return s.lower()
    # elif [x.upper().count(x) for x in s] > [x.lower().count(x) for x in s]:
    #     return s.lower()
    # elif [x.upper().count(x) for x in s] < [x.lower().count(x) for x in s]:
    #     return s.upper()
    # else:
    #     return s.lower()



solve("CODE")