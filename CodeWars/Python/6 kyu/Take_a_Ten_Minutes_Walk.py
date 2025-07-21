def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    x = 0
    y = 0

    for dir in walk:
        if dir == "n":
            y += 1
        elif dir == "s":
            y -= 1
        elif dir == "e":
            x += 1
        elif dir == "w":
            x -= 1
    return x == 0 and y == 0
