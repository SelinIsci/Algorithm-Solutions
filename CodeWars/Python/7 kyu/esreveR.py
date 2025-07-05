def reverse(lst):
    empty_list = list()
    i = len(lst) - 1
    while i >= 0:
        empty_list.append(lst[i])
        i -= 1
    return empty_list
