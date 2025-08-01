def first_non_repeating_letter(s):
    lower_s = s.lower()
    for i, ch in enumerate(s):
        if lower_s.count(lower_s[i]) == 1:
            return ch
    return ""
