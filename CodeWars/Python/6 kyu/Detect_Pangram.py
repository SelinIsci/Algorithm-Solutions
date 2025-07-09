def is_pangram(st):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(st.lower()))
