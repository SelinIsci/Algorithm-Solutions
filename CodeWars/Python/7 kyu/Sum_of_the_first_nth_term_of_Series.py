def series_sum(n):
    total = 0
    for i in range(n):
        total += 1 / (1 + 3 * i)
    return "{:.2f}".format(total)
