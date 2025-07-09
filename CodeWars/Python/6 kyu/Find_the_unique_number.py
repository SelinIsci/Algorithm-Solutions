def find_uniq(arr):
    a, b, c = arr[0], arr[1], arr[2]
    if a == b:
        for n in arr:
            if n != a:
                return n
    else:
        if a == c:
            return b
        else:
            return a
    return n
