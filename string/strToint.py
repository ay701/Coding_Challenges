
def str_to_int(st):

    neg = False
    ret = 0

    if st[0] == "-":
        neg = True
        st = st[1:]

    if len(st) > 1 and st[0] == "0":
        exit("Invalid")

    for i in range(len(st)):

        if not st[i].isdigit():
            exit("Invalid")

        # print(ret, st[i], int(st[i]))
        ret *= 10
        ret += int(st[i])
        print(ret)

    return -1*ret if neg else ret

print str_to_int("-45123")
