# Reverse Integer
# Consider negative number
# Consider the number end with 0


def reverse_int(data):

    output = 0
    neg = False

    if data < 0:
        neg = True
        data = -1 * data

    while data > 0:
        rem = data % 10
        output = output * 10 + rem
        data /= 10
        # print data, rem, output
        
    return output if not neg else -1*output

print reverse_int(456730)
# print reverse_int(53421.23)