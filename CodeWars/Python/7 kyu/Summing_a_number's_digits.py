def sum_digits(number):
    n = abs(number)
    return sum(int(c) for c in str(n))
