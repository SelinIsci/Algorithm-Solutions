import re


def to_camel_case(text):
    words = re.split("[_-]", text)
    if not words:
        return ""
    return words[0] + "".join(word.capitalize() for word in words[1:])
