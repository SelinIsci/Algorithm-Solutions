def squares(x, n):
    if n <= 0:
        return []
    result = [x]
    for _ in range(n - 1):
        result.append(result[-1] ** 2)
    return result
