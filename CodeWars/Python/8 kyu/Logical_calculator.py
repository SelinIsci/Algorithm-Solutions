def logical_calc(array, op):
    if op == "AND":
        result = True
        for b in array:
            result = result and b
        return result
    elif op == "OR":
        result = False
        for b in array:
            result = result or b
        return result
    elif op == "XOR":
        result = False
        for b in array:
            result = result != b
        return result
