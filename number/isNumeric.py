def isNumeric(data):
    point = False

    if data[0]=="-":
        data = data[1:]

    for i in range(len(data)):
   
        if data[i] not in [".","0","1","2","3","4","5","6","7","8","9"]:
            return False

        # point cannot be at start of string
        if data[i]=="." and i==0:
            return False

        # point cannot be at end of string
        if data[i]=="." and i==len(data)-1:
            return False

        # string cannot have mulitiple points
        if point and data[i]==".":
            return False

        if data[i]==".":
            point = True

    return True

print isNumeric("-3.49")
print isNumeric("-.49")
