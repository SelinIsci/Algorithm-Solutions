def divisible_by(numbers, divisor):
    arr = []
    for num in numbers:
        if num % divisor == 0:
            arr.append(num)
    return arr
