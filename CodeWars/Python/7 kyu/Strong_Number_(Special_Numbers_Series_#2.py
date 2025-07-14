import math
def strong_num(number):
    total = sum(math.factorial(int(digit)) for digit in str(number))
    return "STRONG!!!!" if total == number else "Not Strong !!"
