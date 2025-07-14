def solve(s):
    lower = 0
    upper = 0
    for c in s:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
    return s.lower() if upper <= lower else s.upper()
