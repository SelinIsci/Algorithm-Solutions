def number_to_pwr(number, p):
    result = 1
    for i in range(1, p + 1):
        result *= number
    return result
