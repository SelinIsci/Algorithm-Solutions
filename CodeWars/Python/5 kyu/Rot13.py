def rot13(message):
    result = ""
    for ch in message:
        if "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + 13) % 26 + ord("a"))
        elif "A" <= ch <= "Z":
            result += chr((ord(ch) - ord("A") + 13) % 26 + ord("A"))
        else:
            result += ch
    return result
