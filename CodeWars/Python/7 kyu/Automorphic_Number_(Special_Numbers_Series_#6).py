def automorphic(n):
    str_num = str(n**2)
    if str_num.endswith(str(n)):
        return "Automorphic"
    return "Not!!"
