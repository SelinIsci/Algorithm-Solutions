def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x % 2 != 0]

    if len(evens) == 1:
        return evens[0]
    else:
        return odds[0]
