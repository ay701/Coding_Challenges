def combineArrays(L1, L2):
  
    output = []
    L = L1 + L2
    L.sort()
    
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

L1 = [1,4,5,6,10,5,8]
L2 = [1,14,3,16,11,15,8]

print combineArrays(L1,L2)