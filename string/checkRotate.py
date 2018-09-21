# apple 
# pplea
# pleap

def isRotate(a,b):

    if len(a)!=len(b):
        return False

    c = a + a

    cnt = 0

    print c,b
    for i in range(len(c)):   
        print c[i], b[cnt]
        if c[i]==b[cnt]:
            cnt+=1
            print cnt
        else:
            cnt=0
            if c[i]==b[cnt]:
                cnt=1

        if cnt==len(b):
            return True

    return cnt==len(b)

print isRotate("apple","pplea")
print isRotate("apple","pleap")

def isrotation(s1,s2):
     print 2*s1, s2
     return len(s1)==len(s2) and s2 in 2*s1

print isrotation("apple","pplea")
print isrotation("apple","pleap")
