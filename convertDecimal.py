#######################################
# Convert decimal to other base number
# hint: use stack
# Example: 321 -> 101000001 (binary)
#          321 -> 501 (octal)
#          321 -> 141 (hex)
#######################################

def convertDecimal(data, base):
    stack = []
    
    while data:
       rem = data%base 
       stack.append(rem)
       data = data//base

    output = ""

    while stack:
        output += str(stack.pop())

    return output

print(convertDecimal(321,2))
print(convertDecimal(321,8))
print(convertDecimal(321,16))

       
