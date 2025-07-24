def sort_my_string(s):
    odds = []
    evens = []

    for i in range(len(s)):
        if i % 2 == 0:
            evens.append(s[i])
        else:
            odds.append(s[i])

    return "".join(evens) + " " + "".join(odds)
