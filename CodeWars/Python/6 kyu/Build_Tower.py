def tower_builder(n):
    tower = []
    for i in range(n):
        stars = "*" * (2 * i + 1)
        spaces = " " * (n - i - 1)
        tower.append(spaces + stars + spaces)
    return tower
