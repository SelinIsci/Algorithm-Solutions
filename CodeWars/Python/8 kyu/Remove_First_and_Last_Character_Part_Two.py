def array(string):
    new_s = string.split(",")
    if len(new_s) <= 2:
        return None
    return " ".join(new_s[1:-1])
