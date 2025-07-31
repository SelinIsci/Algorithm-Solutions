def generate_range(start, stop, step):
    if step == 0:
        raise ValueError("Step cannot be zero.")
    if step > 0:
        return list(range(start, stop + 1, step))
    else:
        return list(range(start, stop - 1, step))
