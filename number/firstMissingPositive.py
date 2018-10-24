# LeetCode Q41
# Given an unsorted integer array, find the first missing positive integer.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Your algorithm should run in O(n) time and uses constant space.
# Thoughts:
# Swap the number to make l[i]=i+1, scan the list and return first l[i] which is not i+1

import collections


def first_missing_positive(l):

    n = len(l)

    if n == 0:
        return 1

    for i in range(n):
        if l[i] in range(1, n+1) \
                and l[i] != i+1 \
                and l[l[i]-1] != l[i]:
            tmp = l[l[i]-1]
            l[l[i]-1] = l[i]
            l[i] = tmp

    for i in range(n):
        if l[i] != i+1:
            return i+1

    return l[-1]+1  # if not found, return last element

l = [2, 1, 3, 9, 5]

print first_missing_positive(l)

######
# https://codereview.stackexchange.com/questions/149270/given-an-unsorted-integer-array-find-the-first-missing-positive-integer
######

def first_missing_positive_2(l):

    dic = collections.defaultdict(int)
    n = len(l)

    for e in l:
        dic[e] = 1

    for i in range(1, n+1):
        if dic.get(i) == 0:
            return i

    return n+1

l2 = [2, 1, 3, 9, 5]

print first_missing_positive(l2)

