import math


def square_or_square_root(arr):
    return [int(math.sqrt(n)) if math.sqrt(n).is_integer() else n * n for n in arr]
