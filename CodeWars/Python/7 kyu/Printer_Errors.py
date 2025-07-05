def printer_error(s):
    errors = 0
    for ch in s:
        if ch < "a" or ch > "m":
            errors += 1
    return f"{errors}/{len(s)}"
