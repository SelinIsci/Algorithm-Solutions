def wave(people):
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            waved = people[:i] + people[i].upper() + people[i + 1 :]
            result.append(waved)
    return result
