def no_odds(values):
    arr = []

    for i in values:
        if i % 2 == 0:
            arr.append(i)
    return arr
