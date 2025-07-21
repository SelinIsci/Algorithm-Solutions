def tribonacci(signature, n):
    result = signature[:n]
    while len(result) < n:
        next_value = sum(result[-3:])
        result.append(next_value)
    return result
