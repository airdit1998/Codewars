def how_much_water(L, X, N):
    """
    L - water
    X - Load of washing machine
    N - clothes
    """
    if X * 2 < N:
        return 'Too much clothes'
    elif X > N:
        return 'Not enough clothes'
    else:
        return round(L * (1.1 ** (N - X)), 2)
