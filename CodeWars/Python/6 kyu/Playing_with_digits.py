def dig_pow(n, p):
    digits = [int(d) for d in str(n)]
    total = sum(digit ** (p + i) for i, digit in enumerate(digits))

    if total % n == 0:
        return total // n
    else:
        return -1
