def title_case(title, minor_words=""):
    if not title:
        return ""
    minor_words_set = set(minor_words.lower().split())
    words = title.lower().split()
    result = []

    for i, word in enumerate(words):
        if i == 0:
            result.append(word.capitalize())
        elif word in minor_words_set:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)
