import math


def nearest_sq(n):
    root = math.isqrt(n)
    if root * root == n:
        return n
    low_sq = root**2
    up_sq = (root + 1) * (root + 1)

    if n - low_sq <= up_sq - n:
        return low_sq
    else:
        return up_sq
