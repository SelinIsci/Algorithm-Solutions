def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new_string = ""
    for c in string_:
        if c not in vowels:
            new_string += c
    return new_string
