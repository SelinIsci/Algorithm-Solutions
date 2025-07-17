def switcher(arr):
    special_chars = {"27": "!", "28": "?", "29": " "}
    result = ""
    for num in arr:
        if num in special_chars:
            result += special_chars[num]
        else:
            letter = chr(123 - int(num))
            result += letter
    return result
