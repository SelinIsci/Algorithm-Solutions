def adjacent_element_product(array):
    max = array[0] * array[1]

    for i in range(0, len(array) - 1):
        product = array[i] * array[i + 1]
        if product > max:
            max = product

    return max
