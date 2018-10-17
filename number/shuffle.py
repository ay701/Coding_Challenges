# Shuffle an array of numbers without duplicates
# leetcode

import random


def shuffle(L):

    n = len(L)
    print L

    for i in range(n-1, -1, -1):
        tmp = L[i]
        k = random.randint(0, i)
        L[i] = L[k]
        L[k] = tmp

    return L

print shuffle([3, 1, 2, 5, 6, 9, 0, 7])
