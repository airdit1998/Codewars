def power_sumDigTerm(n):
    """shit kata"""
    i = 11
    digterm_list = []
    while i < 1000000:
        split_dgt = list(str(i))
        sum_split_dgt = sum([int(x) for x in split_dgt])
        if sum_split_dgt ** len(split_dgt) - 1 == i:
            digterm_list.append(i)
        i += 1
        #break
    return digterm_list

print(power_sumDigTerm(4))