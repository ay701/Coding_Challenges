#######################################
# Convert decimal to other base number
# hint: use stack
# Example: 321 -> 101000001 (binary)
#          321 -> 501 (octal)
#          321 -> 141 (hex)
#######################################


def convert_decimal_to_other_bases(data, base):
    stack = []
    
    while data:
        rem = data % base
        stack.append(rem)
        data = data//base

    output = ""

    while stack:
        output += str(stack.pop())

    return output

print(convert_decimal_to_other_bases(321, 2))
print(convert_decimal_to_other_bases(321, 8))
print(convert_decimal_to_other_bases(321, 16))
