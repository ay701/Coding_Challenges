
# [10,1,15,2,3,5,1,3]

def findMaxAfterMin(L):

    if len(L)<=1:
        return None

    cur = L[0]
    min_ = cur
    max_ = None

    for i, nex in enumerate(L[1:]):

        if cur<min_:
            min_ = cur
            
            if nex > cur:
                max_ = nex
            else:
                max_ = None

        elif cur==min_:
            if max_ is None or nex>max_:
                max_ = nex
        
        cur = nex
 
    return max_

print findMaxAfterMin([10,1,15,2,3,5,1,3,10,1,16,2,3,5,1,3])

