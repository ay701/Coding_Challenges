#######################################
# Convert decimal to other base number
# hint: use stack
#######################################

def convertDecimal(data, base):
    stack = []
    
    while data:
       rem = data%base 
       stack.append(rem)
       data = data//base
       print stack

    output = ""

    while stack:
        output += str(stack.pop())

    return output

print(convertDecimal(321,2))

       
