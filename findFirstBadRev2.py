
# 1,2,3, 4, 5,...25.....50...100
#        |  |            |
#       Bad bad  good       bad


#       log100


def findFirstBadRev(start,n):

    firstBadRev = -1

    if n in [1,2] and isBad(start+n):
        return start+n
    
    end = start + n

    while end>start+1:

        mid = (start+end)//2

        if isBad(mid):
            end = mid
        else:
            start = mid+1
        
        print start, end

    if isBad(start):
        firstBadRev = start
    elif isBad(end):
        firstBadRev = end

    return firstBadRev


def isBad(n):

    if n in [7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
        return True

    return False

print findFirstBadRev(5,10)







