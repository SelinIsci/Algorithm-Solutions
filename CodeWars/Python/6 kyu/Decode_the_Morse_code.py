from preloaded import MORSE_CODE


def decode_morse(morse_code):
    morse_code = morse_code.strip()
    words = morse_code.split("   ")

    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = [MORSE_CODE[char] for char in letters]
        decoded_words.append("".join(decoded_letters))
    return " ".join(decoded_words)
