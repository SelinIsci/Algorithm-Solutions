def find_smallest(numbers, to_return):
    smallest_value = min(numbers)
    if to_return == "value":
        return smallest_value
    elif to_return == "index":
        return numbers.index(smallest_value)
