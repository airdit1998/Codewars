def get_score(n):
    start = 50
    if n == 1:
        return start
    val = 50
    for i in range(1, n):
        val += 50
        start += val

    return start
