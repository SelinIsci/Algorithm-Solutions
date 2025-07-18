def min_value(digits):
    unique_digit = sorted(set(digits))
    return int("".join(str(d) for d in unique_digit))
