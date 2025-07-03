def switcheroo(s):
    result = ""
    for c in s:
        if c == "a":
            result += "b"
        elif c == "b":
            result += "a"
        else:
            result += "c"
    return result
