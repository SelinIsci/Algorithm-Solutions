def two_highest(arg1):
    list = sorted(set(arg1), reverse=True)
    return list[:2]
