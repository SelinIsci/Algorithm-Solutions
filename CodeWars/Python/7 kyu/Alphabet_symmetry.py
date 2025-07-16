def solve(strings: list[str]) -> list[int]:
    result = []
    for word in strings:
        count = 0
        for i, ch in enumerate(word, start=1):
            if (ord(ch.lower()) - ord("a") + 1) == i:
                count += 1
        result.append(count)
    return result
