def max_sequence(arr):
    max_sum = 0
    current_sum = 0

    for number in arr:
        current_sum += number
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
