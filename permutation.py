def permutation(st):

    n = len(st)

    for i in range(n):
        for j in range(n):
            print st[i] + st[0:i] + st[i+1:]
            print st[0:i+1] + st[i] + st[i+1:]
            print st[i+1:] + st[0:i] + st[i]

#print permutation('yes')

def permutation_recur(prefix,st):

    cnt = len(st)

    if cnt==0 :
        print prefix
    else:
        for i in range(cnt):
            permutation_recur(prefix+st[i],st[0:i]+st[i+1:])

#print permutation_recur('','hi')
print permutation_recur('','hie')
#print permutation_recur('','hiar')
#print permutation_recur('','135')
