def get_middle(s):
    n = len(s)
    middle = n // 2
    if n % 2 == 1:
        return s[middle]
    else:
        return s[middle - 1] + s[middle]
