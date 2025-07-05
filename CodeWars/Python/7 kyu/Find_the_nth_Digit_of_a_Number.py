def find_digit(num, nth):
    num = abs(num)

    if nth <= 0:
        return -1

    digit = (num // (10 ** (nth - 1))) % 10
    return digit
