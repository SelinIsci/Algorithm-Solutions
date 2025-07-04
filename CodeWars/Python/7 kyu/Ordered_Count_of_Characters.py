def ordered_count(inp):
    result = []
    seen = set()

    for char in inp:
        if char not in seen:
            result.append((char, inp.count(char)))
            seen.add(char)

    return result
