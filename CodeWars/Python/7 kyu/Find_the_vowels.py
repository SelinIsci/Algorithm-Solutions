def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    res = []
    for i, c in enumerate(word):
        if c in vowels:
            res.append(i + 1)
    return res
