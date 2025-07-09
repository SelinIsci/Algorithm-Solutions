def pairs(arr):
    count = 0
    for i in range(0, len(arr) - 1, 2):
        if abs(arr[i] - arr[i + 1]) == 1:
            count += 1
    return count
