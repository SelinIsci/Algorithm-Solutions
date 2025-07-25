def find_nb(m):
    n = 0
    total = 0

    while total < m:
        n += 1
        total += n**3
    return n if total == m else -1
