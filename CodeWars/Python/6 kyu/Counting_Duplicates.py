def duplicate_count(text):
    text = text.lower()
    seen = set()
    duplicates = set()

    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return len(duplicates)
