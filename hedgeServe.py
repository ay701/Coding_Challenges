#python 2.7.6

print "Hello, world!"

# 2,1 = 2
# 2,2 = 4 = power(2,1) * = power(2,1) * 2
# 2,3 = 8 = power(2,1) * 2
# 2,4 = 16 = power(2,2) * power(2,2)
# 2,5 = 16 = power(2,2) * power(2,2) * 2

def power_(m, n):
    
    neg = False
    rtn = 0
    
    if n<0:
        neg = True
        n = -1*n
    
    if n==0:
        return 1
    
    if n==1:
        return m
    
    tmp = power_(m, n/2)
    rtn = tmp * tmp if n%2==0 else tmp * tmp * m 
       
    return 1/float(rtn) if neg else rtn
    
print power_(2,3)
print power_(5,2)
print power_(5,-2)
