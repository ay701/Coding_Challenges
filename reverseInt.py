# Reverve Integer
# Consider negative number
# Consider the number end with 0

def reverseInt(data):

    output = 0
    neg = False

    if data<0:
    	neg = True
    	data = -1*data

    while data>0:
        remd = data%10
        output = output*10 + remd
        data = data/10
        # print data, remd, output 
        
    return output if not neg else -1*output

print reverseInt(456730)
# print reverseInt(53421.23)