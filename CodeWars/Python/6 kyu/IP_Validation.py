def is_valid_IP(strng):
    ip_parts = strng.split(".")
    if len(ip_parts) != 4:
        return False
    for part in ip_parts:
        if not part.isdigit():
            return False
        if part != "0" and part.startswith("0"):
            return False
        num = int(part)
        if not (0 <= num <= 255):
            return False

    return True
