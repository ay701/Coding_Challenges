# apple 
# pplea
# pleap

def isRotate(a,b):

    if len(a)!=len(b):
        return False

    c = a + a

    cnt = 0

    for i in range(len(c)):   
        if c[i]==b[cnt]:
            cnt+=1
        else:
            cnt=0

        if cnt==len(b):
            return True

    return cnt==len(b)

print isRotate("apple","pplea")
print isRotate("apple","pleap")
