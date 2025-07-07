def kebabize(st):
    result = ""
    for c in st:
        if c.isdigit():
            continue
        if c.isupper():
            if result != "":
                result += "-"
            result += c.lower()
        else:
            result += c
    return result
