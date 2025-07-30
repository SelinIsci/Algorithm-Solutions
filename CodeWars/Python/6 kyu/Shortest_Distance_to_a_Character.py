def shortest_to_char(s, c):
    if not s or c == "" or c not in s:
        return []

    n = len(s)
    res = [float("inf")] * n

    prev = float("-inf")
    for i in range(n):
        if s[i] == c:
            prev = i
        res[i] = i - prev

    prev = float("inf")
    for i in reversed(range(n)):
        if s[i] == c:
            prev = i
        res[i] = min(res[i], prev - i)

    return res
