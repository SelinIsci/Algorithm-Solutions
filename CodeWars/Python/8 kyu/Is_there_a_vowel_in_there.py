def is_vow(inp):
    vowels = {97, 101, 105, 111, 117}
    return [chr(i) if i in vowels else i for i in inp]
