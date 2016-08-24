# Shuffle an array of numbers without duplicates
import random

def shuffle(L):
    print L
    for i in range(len(L)-1, -1, -1):
        tmp = L[i]
        k = random.randint(0,i) 
        L[i] = L[k]
        L[k] = tmp

    return L

print shuffle([3,1,2,5,6,9,0,7])
