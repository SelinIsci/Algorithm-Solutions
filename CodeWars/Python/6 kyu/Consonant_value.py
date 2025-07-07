def solve(s):
    max_val = 0
    parts = []
    current = ""

    for c in s:
        if c not in "aeiou":
            current += c
        else:
            if current:
                parts.append(current)
                current = ""
    if current:
        parts.append(current)

    for part in parts:
        total = sum(ord(c) - 96 for c in part)
        max_val = max(max_val, total)

    return max_val
