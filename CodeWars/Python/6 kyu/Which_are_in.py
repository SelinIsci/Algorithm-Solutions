def in_array(array1, array2):
    return sorted({word for word in array1 if any(word in target for target in array2)})
