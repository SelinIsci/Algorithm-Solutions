def two_sum(numbers, target):
    d = {num: i for i, num in enumerate(numbers)}
    for i in range(len(numbers)):
        value = target - numbers[i]
        if value in d and d[value] != i:
            return [i, d[value]]
