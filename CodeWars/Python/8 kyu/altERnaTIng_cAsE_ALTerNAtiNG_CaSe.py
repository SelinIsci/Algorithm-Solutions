def to_alternating_case(string):
    res = []

    for c in string:
        if c.isupper():
            res.append(c.lower())
        elif c.islower():
            res.append(c.upper())
        else:
            res.append(c)
    return "".join(res)
