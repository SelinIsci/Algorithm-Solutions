def solve(arr):
    seen = set()
    result = []

    for i in reversed(arr):
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result[::-1]
