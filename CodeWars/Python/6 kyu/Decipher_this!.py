def decipher_this(s):
    words = s.split(" ")
    decoded_words = []

    for word in words:
        i = 0
        while i < len(word) and word[i].isdigit():
            i += 1
        asc_code = int(word[:i])
        first_letter = chr(asc_code)

        rest = list(word[i:])

        if len(rest) > 1:
            rest[0], rest[-1] = rest[-1], rest[0]
        decoded_word = first_letter + "".join(rest)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)
