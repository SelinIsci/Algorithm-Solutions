def stairs_in_20(stairs):
    one_year_total = sum(sum(day) for day in stairs)
    return one_year_total * 20
