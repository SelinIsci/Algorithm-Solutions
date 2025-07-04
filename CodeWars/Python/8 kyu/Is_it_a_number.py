import re


def is_digit(s):
    pattern = r"^[+-]?\d+(\.\d+)?$"
    return bool(re.fullmatch(pattern, s.strip()))
