def valid_braces(string):
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{"}

    for ch in string:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != brackets_map[ch]:
                return False
            stack.pop()
    return not stack
