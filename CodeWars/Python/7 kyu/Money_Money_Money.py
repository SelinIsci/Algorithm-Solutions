def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        earned = principal * interest
        taxed = earned * tax
        principal += earned - taxed
        years += 1
    return years
