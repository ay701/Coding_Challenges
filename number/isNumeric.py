def is_numeric(data):
    point = False

    if data[0] == "-":
        data = data[1:]

    n = len(data)

    for i in range(n):

        # point cannot be at start of string
        if data[0] == "." or data[n-1] == ".":
            return False

        if data[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False

        # string cannot have multiple points
        if point and data[i] == ".":
            return False

        if data[i] == ".":
            point = True

    return True

print is_numeric("-3.49")
print is_numeric("-.49")
