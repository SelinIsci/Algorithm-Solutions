def unique_in_order(sequence):
    result = []
    previous = object()
    for i in sequence:
        if i != previous:
            result.append(i)
            previous = i
    return result
