def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return "0=0"
    else:
        numbers = [str(i) for i in range(n + 1)]
        total = sum(range(n + 1))
        return "+".join(numbers) + f" = {total}"
