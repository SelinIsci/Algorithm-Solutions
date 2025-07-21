def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            position = ord(char) - ord("a") + 1
            result.append(str(position))
    return " ".join(result)
