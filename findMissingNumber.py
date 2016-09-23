def findMissingNumber(L):

    x1 = L[0]
    x2 = 1

    for i in range(1,len(L)):
        x1 = x1^L[i]

    for i in range(2,len(L)+2):
        x2 = x2^i

    return x1^x2

print findMissingNumber([1,2,3,4,5,7,8,9,10])


def findMissingNumber2(L):

    n = len(L)

    sum_ = (n+1)*(n+2)//2

    for i in L:
        sum_ -= i

    return sum_

print findMissingNumber2([1,2,3,4,5,7,8,9,10])
