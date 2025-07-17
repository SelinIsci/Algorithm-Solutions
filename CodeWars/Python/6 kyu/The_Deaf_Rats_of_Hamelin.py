def count_deaf_rats(town):
    town = town.replace(" ", "")
    piper_index = town.index("P")

    left = town[:piper_index]
    right = town[piper_index + 1 :]

    left_rats = [left[i : i + 2] for i in range(0, len(left), 2)]
    right_rats = [right[i : i + 2] for i in range(0, len(right), 2)]

    deaf_count = 0
    for rat in left_rats:
        if rat == "O~":
            deaf_count += 1
    for rat in right_rats:
        if rat == "~O":
            deaf_count += 1
    return deaf_count
