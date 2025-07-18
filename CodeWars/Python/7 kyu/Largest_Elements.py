def largest(n, xs):
    if n <= 0:
        return []
    xs.sort()
    return xs[-n:]
