def flatten_and_sort(array):
    list = []
    for i in array:
        for j in i:
            list.append(j)
    list.sort()
    return list
