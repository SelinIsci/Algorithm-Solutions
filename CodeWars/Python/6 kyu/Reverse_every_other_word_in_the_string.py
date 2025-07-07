def reverse_alternate(st):
    parts = st.split()
    for i in range(len(parts)):
        if i % 2 == 1:
            parts[i] = parts[i][::-1]
    return " ".join(parts)
