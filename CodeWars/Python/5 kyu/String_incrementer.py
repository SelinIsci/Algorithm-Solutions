def increment_string(s):
    head = s.rstrip("0123456789")
    tail = s[len(head) :]

    if tail == "":
        return s + "1"

    number_len = len(tail)
    incremented = str(int(tail) + 1).zfill(number_len)
    return head + incremented
