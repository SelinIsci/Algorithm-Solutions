def max_product(lst, n_largest_elements):
    res = 1
    lst.sort(reverse=True)
    for i in range(n_largest_elements):
        res *= lst[i]
    return res
