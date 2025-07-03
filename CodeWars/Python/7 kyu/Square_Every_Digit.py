def square_digits(num):
    num = str(num)
    res = []
    for c in range(0, len(num)):
        res.append(str(int(num[c]) ** 2))
    return int("".join(res))
