def rotateString(L, k):
    
    if L is None or len(L)==0 :
    	exit("Error input")

    if k>len(L):
    	k = k%len(L)

    L_ = []

    i = k
    while i>0:
    	L_.append(L[-i])
    	i-=1
    
    i = 0
    while i<len(L)-k:
        L_.append(L[i])
        i+=1

    return L_

L = [2,3,4,5,6,7]
k = 10

print rotateString(L,k)

################
# Use reversal
################
def rotateString_(L,k):

    piv = len(L)-k
    L1 = L[0:piv]
    L2 = L[piv:len(L)]
    L1 = reverse(L1)
    L2 = reverse(L2)
    return reverse(L1+L2)

def reverse(L):

    left = 0
    right = len(L)

    while left<right:
    	tmp = L[left]
    	L[left] = L[right-1]
    	L[right-1] = tmp
    	left += 1
        right -= 1

    return L

L = [2,3,4,5,6,7]
k = 10

print rotateString_(L,k)