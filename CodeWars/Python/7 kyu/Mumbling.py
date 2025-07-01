def accum(st):
    arr = []
    for i in range(len(st)):
        c = st[i]
        arr.append(c.upper() + c.lower() * i)
    return "-".join(arr)
