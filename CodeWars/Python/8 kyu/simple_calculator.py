def calculator(x, y, op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"

    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "/":
        return x / y
    elif op == "*":
        return x * y
    else:
        return "unknown value"
