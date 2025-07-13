def array_leaders(numbers):
    result = []
    for i in range(len(numbers)):
        right_sum = sum(numbers[i + 1 :])
        if numbers[i] > right_sum:
            result.append(numbers[i])
    return result
