def max_tri_sum(numbers):
    unique_num = set(numbers)
    max_three = sorted(unique_num, reverse=True)[:3]
    return sum(max_three)
