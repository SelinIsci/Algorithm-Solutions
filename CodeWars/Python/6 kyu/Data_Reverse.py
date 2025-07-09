def data_reverse(data):
    bytes = [data[i : i + 8] for i in range(0, len(data), 8)]

    reversed_bytes = bytes[::-1]
    return [bit for byte in reversed_bytes for bit in byte]
