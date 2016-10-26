# Write a function (with helper functions if needed) called to Excel 
# that takes an excel column value (A,B,C,D,AA,AB,AC, AAA..) and returns a corresponding integer value (A=1,B=2,AA=27..)

def excelColumnToNumber(st):

    output = 0
    leng = len(st) 
    i = 0 

    while st:
    	tmp = ord(st[-1]) - 64
    	output += tmp * pow(26,i)
        st = st[:-1]
        i+=1

    return output

print excelColumnToNumber("AA")