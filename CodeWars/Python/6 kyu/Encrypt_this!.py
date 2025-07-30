def encrypt_this(text):
    def encrypt_word(word):
        if not word:
            return ""
        first_ascii = str(ord(word[0]))
        if len(word) == 1:
            return first_ascii
        elif len(word) == 2:
            return first_ascii + word[1]
        else:
            second = word[1]
            last = word[-1]
            middle = word[2:-1]
            return first_ascii + last + middle + second

    return " ".join(encrypt_word(word) for word in text.split())
