def min_sum(arr):
    arr.sort()
    total = 0
    n = len(arr)
    for i in range(n // 2):
        total += arr[i] * arr[n - 1 - i]
    return total
