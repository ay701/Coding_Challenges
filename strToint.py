
def strToInt(st):

    neg = False
    ret = 0

    for i in range(len(st)):

        asc = ord(st[i])

        if i==0 and st[i]=="-":
            neg = True
            continue

        if i==0 and asc==48 and len(st)>1:
            exit("Invalid")

        if i and asc<48 or asc>72:
            exit("Invalid")

        ret *= 10
        ret = ret + asc - 48 

    return -1*ret if neg else ret

print strToInt("-45123")
