def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    return 0
