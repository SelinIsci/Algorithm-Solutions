def sum_of_differences(arr):
    arr.sort(reverse=True)
    total = 0
    for i in range(len(arr) - 1):
        total += arr[i] - arr[i + 1]
    return total
