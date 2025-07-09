def string_clean(s):
    str = ""
    for c in s:
        if c.isdigit():
            str += ""
        else:
            str += c
    return str
