def solution(s):
    new_st = []

    for c in s:
        if c.islower():
            new_st.append(c)
        else:
            new_st.append(f" {c}")
    return "".join(new_st)
