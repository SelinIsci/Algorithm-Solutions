def explode(s):
    new_str = ""
    for ch in s:
        new_str += ch * int(ch)
    return new_str
