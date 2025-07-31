def clonewars(kata_per_day):
    clones = 1
    total_kata = 0
    capacity = kata_per_day

    while capacity > 0:
        total_kata += clones * capacity
        capacity -= 1
        if capacity > 0:
            clones *= 2

    return [clones, total_kata]
