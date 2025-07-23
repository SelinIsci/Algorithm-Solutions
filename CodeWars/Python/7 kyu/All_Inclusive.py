def contain_all_rots(strng, arr):
    if strng == "":
        return True
    return all(strng[i:] + strng[:i] in arr for i in range(len(strng)))
