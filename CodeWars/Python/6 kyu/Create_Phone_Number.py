def create_phone_number(n):
    return f"({''.join(str(num) for num in n[:3])}) {''.join(str(num) for num in n[3:6])}-{''.join(str(num) for num in n[6:])}"
