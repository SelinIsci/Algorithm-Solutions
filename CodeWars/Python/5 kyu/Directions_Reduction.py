def dir_reduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    for dir in arr:
        if stack and opposite[dir] == stack[-1]:
            stack.pop()
        else:
            stack.append(dir)

    return stack
