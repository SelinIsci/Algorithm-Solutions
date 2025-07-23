def rgb(r, g, b):
    def clamp(value):
        return max(0, min(255, value))

    return f"{clamp(r):02X}{clamp(g):02X}{clamp(b):02X}"
