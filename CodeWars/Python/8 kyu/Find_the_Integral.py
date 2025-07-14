def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent
    return f"{new_coefficient}x^{new_exponent}"
