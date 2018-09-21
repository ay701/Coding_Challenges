def mergeSortedArrays(L1,L2):

    L = []

    if len(L1)==0:
    	return L2

    if len(L2)==0:
    	return L1

    i,j = 0,0

    while i<len(L1) and j<len(L2):

    	if L1[i]<L2[j]:
    		L.append(L1[i])
    		i += 1
    	elif L1[i]>L2[j]:
    		L.append(L2[j])
    		j += 1
    	else:
    		L.append(L1[i])
    		i += 1
    		j += 1

    for e in L1[i:]:
        L.append(e)

    for e in L2[j:]:
        L.append(e)

    return L

print mergeSortedArrays([2,3,4,5],[4,5,6,7])