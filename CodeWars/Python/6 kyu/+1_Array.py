def up_array(arr):
    if not arr:
        return None
    for x in arr:
        if type(x) != int or x < 0 or x > 9:
            return None

    i = len(arr) - 1
    while i >= 0:
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0
        i -= 1
    return [1] + arr
