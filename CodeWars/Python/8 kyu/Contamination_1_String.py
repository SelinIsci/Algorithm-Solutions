def contamination(text, char):
    len_text = len(text)
    new_text = []
    for i in range(0, len_text):
        new_text.append(char)
    return "".join(new_text)
