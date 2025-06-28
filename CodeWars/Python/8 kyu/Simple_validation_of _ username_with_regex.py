import re

pattern = r"^[a-z0-9_]{4,16}$"


def validate_usr(username):
    return bool(re.match(pattern, username))
