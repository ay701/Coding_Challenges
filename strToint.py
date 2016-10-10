
def strToInt(st):

    neg = False
    ret = 0

    if st[0]=="-":
        neg = True
        st = st[1:]

    if len(st)>1 and st[0]=="0":
        exit("Invalid")

    for i in range(len(st)):

        asc = ord(st[i])

        if asc<48 or asc>72:
            exit("Invalid")

        ret *= 10
        ret = ret + asc - 48 

    return -1*ret if neg else ret

print strToInt("-45123")
