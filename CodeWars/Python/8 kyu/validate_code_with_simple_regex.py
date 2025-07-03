import re


def validate_code(code):
    code = str(code)
    return bool(re.match(r"^[1-3]", code))
