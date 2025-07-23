def parse_float(string):
    try:
        if isinstance(string, list):
            string = "".join(string)
        return float(string)
    except (ValueError, TypeError):
        return None
