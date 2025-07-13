def spin_words(sentence):
    parts = sentence.split()
    new_s = []

    for c in parts:
        if len(c) >= 5:
            new_s.append("".join(reversed(c)))
        else:
            new_s.append(c)

    return " ".join(new_s)
