def cube_odd(arr):
    for x in arr:
        if not isinstance(x, int) or isinstance(x, bool):
            return None
    return sum(x**3 for x in arr if x % 2 != 0)
