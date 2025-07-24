def delete_nth(order, max_e):
    counts = {}
    result = []
    for num in order:
        if counts.get(num, 0) < max_e:
            result.append(num)
            counts[num] = counts.get(num, 0) + 1
    return result
