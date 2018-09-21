#######################################
# Convert decimal to other base number
# hint: use stack
# Example: 321 -> 101000001 (binary)
#          321 -> 501 (octal)
#          321 -> 141 (hex)
#######################################

def convertDecimalToOtherBases(data, base):
    stack = []
    
    while data:
       rem = data%base 
       stack.append(rem)
       data = data//base

    output = ""

    while stack:
        output += str(stack.pop())

    return output

print(convertDecimalToOtherBases(321,2))
print(convertDecimalToOtherBases(321,8))
print(convertDecimalToOtherBases(321,16))

       
