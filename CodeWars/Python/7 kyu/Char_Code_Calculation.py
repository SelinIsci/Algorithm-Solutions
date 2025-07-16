def calc(s):
    total1 = "".join(str(ord(ch)) for ch in s)
    total2 = total1.replace("7", "1")
    sum_total1 = sum(int(d) for d in total1)
    sum_total2 = sum(int(d) for d in total2)
    return sum_total1 - sum_total2
