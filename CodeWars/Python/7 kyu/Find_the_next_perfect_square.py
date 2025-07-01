import math


def find_next_square(sq):
    num = math.sqrt(sq)

    if num.is_integer():
        return (num + 1) ** 2
    else:
        return -1
