def high(x):
    words = x.split()
    max = 0
    best_word = ""
    for word in words:
        score = sum(ord(c) - ord("a") + 1 for c in word)
        if score > max:
            max = score
            best_word = word

    return best_word
