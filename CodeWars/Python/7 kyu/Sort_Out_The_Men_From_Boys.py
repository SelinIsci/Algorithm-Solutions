def men_from_boys(arr):
    arr = list(set(arr))
    odds = sorted([x for x in arr if x % 2 == 1], reverse=True)
    evens = sorted([x for x in arr if x % 2 == 0])

    return evens + odds
