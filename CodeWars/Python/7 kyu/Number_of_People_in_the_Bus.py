def number(bus_stops):
    total = 0

    for a, b in bus_stops:
        total += a - b
    return total
