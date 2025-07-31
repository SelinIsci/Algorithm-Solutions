def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    for _ in range(n):
        half = len(encrypted_text) // 2
        odd = encrypted_text[:half]
        even = encrypted_text[half:]
        decrypted = []

        for i in range(len(encrypted_text)):
            if i % 2 == 0:
                decrypted.append(even[i // 2])
            else:
                decrypted.append(odd[i // 2])
        encrypted_text = "".join(decrypted)
    return encrypted_text


def encrypt(text, n):
    if not text or n <= 0:
        return text
    for _ in range(n):
        odd = text[1::2]
        even = text[0::2]
        text = odd + even
    return text
