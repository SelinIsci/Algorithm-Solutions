def order(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    sorted_words = sorted(
        words, key=lambda word: [int(ch) for ch in word if ch.isdigit()][0]
    )
    return " ".join(sorted_words)
