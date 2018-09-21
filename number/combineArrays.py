def combineArrays(L1, L2):
  
    output = []
    L = L1 + L2
    # L.sort()
    L = mergeSort(L)
    #print L
    #exit()
    
    if len(L)<=1:
    	return L

    cur = L[0]
    output.append(cur)

    for i, nex in enumerate(L[1:]):
    	if cur==nex:
             continue

        cur = nex        
        output.append(cur)

    return output

def mergeSort(L):

    output = []

    if len(L)<2:
    	return L

    mid = int(len(L)/2)
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])

    mergeSort(left)
    mergeSort(right)
    
    i = 0
    j = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
    	    output.append(left[i])
            i += 1
        else:
    	    output.append(right[j])
            j += 1

    output += left[i:] + right[j:]
    return output

L1 = [1,4,5,6,10,5,8]
L2 = [1,14,3,16,11,15,8]

#print combineArrays(L1,L2)


# Use list comprehension
# But this will not remove duplicates from individual list
def combineArrays1(L1, L2):

    output = L1
    output.extend([x for x in L2 if x not in output])
    return output

print combineArrays1(L1,L2)

# Use set
def combineArrays2(L1, L2):

    s1 = set(L1)
    s2 = set(L2)

    return list(s2) + list(s1 - s2)

print combineArrays2(L1,L2)

