def sort_array(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0])

    result = []
    odd_index = 0

    for x in source_array:
        if x % 2 == 0:
            result.append(x)
        else:
            result.append(odds[odd_index])
            odd_index += 1
    return result
