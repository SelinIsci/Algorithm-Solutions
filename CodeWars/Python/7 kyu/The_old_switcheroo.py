def vowel_2_index(string):
    vowels = "aeiouAEIOU"
    new_str = ""
    for i, c in enumerate(string, 1):
        if c in vowels:
            new_str += str(i)
        else:
            new_str += c
    return new_str
