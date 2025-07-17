def solve(s):
    vowels = "aeiou"
    max_len = current_len = 0

    for ch in s:
        if ch in vowels:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len
