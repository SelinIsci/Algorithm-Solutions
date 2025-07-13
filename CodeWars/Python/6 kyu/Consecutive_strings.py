def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""

    longest = ""
    max_len = 0

    for i in range(n - k + 1):
        current = "".join(strarr[i : i + k])
        if len(current) > max_len:
            max_len = len(current)
            longest = current

    return longest
