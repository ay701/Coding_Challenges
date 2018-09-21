# LeetCode Q41
# Given an unsorted integer array, find the first missing positive integer.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Your algorithm should run in O(n) time and uses constant space.
# Thoughts:
# Swap the number to make l[i]=i+1, scan the list and return first l[i] which is not i+1

def firstMissingPositive(l):

    length = len(l)

    if length==0:
        return 1

    for i in range(length):
        if l[i] in range(1,length+1) and l[i]!=i+1 and l[l[i]-1]!=l[i]:
            tmp = l[l[i]-1]
            l[l[i]-1] = l[i]
            l[i] = tmp

    for i in range(len(l)):
    	if l[i]!=i+1:
    		return i+1

    return l[-1]+1

l = [2,1,3,9,5]

print firstMissingPositive(l)
