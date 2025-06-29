def remove(st, n):
    new_t = ""
    count = 0
    for c in st:
        if c == "!" and count < n:
            count += 1
        else:
            new_t += c
    return new_t
