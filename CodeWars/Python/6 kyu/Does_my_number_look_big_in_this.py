def narcissistic(value):
    digits = [int(d) for d in str(value)]
    power = len(digits)
    total = sum(d**power for d in digits)
    return total == value
