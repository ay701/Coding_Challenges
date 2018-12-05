# Recursion
def permutation(st):
    if len(st) <= 1:
        return [st]

    output = []

    for i, e in enumerate(st):
        for p in permutation(st[:i]+st[i+1:]):
            output.append(p+e)

    return output

print permutation("yesa")


# Iteration
def permute_iter(st):
    
    length = len(st)

    if length <= 1:
        return [st]
    
    output = [st[0]]
    st = st[1:]
    tmp = []
    
    for i, e in enumerate(st):
        for p in output:
            for j in range(len(p)):
                # print tmp, e
                tmp.append(p[0:j]+e+p[j:])
            tmp.append(p+e)

        output = tmp
        tmp = []

    return output

# print permute_iter("yesd")
