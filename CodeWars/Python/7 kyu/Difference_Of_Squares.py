def difference_of_squares(n):
    sum_of_num = n * (n + 1) // 2
    sq_of_sum = sum_of_num**2
    sum_of_sq = n * (n + 1) * (2 * n + 1) // 6
    return sq_of_sum - sum_of_sq
