def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    len_a1 = list(map(len, a1))
    len_a2 = list(map(len, a2))

    return max(abs(max(len_a1) - min(len_a2)), abs(max(len_a2) - min(len_a1)))
