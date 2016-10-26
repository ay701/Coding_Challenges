# You are given a list of numbers. When you reach the end of the list you will come back to the beginning of the list (a circular list). 
# Write the most efficient algorithm to find the minimum # in this list. 
# Find any given # in the list. The numbers in the list are always increasing but you dont know where the circular list begins, 
# ie: 38, 40, 55, 89, 6, 13, 20, 23, 36.

def findMinInCircularList(L):
 
    cnt = len(L)
    
    if cnt==1:
    	return L[0]
    elif cnt==2:
    	return L[0] if L[0]<L[1] else L[1]
    else:
        mid = cnt//2

        print L[mid-1],L[mid],L[mid+1]

        if L[mid]<L[mid+1] and L[mid]<L[mid-1]:
        	return L[mid]

        if L[mid]>L[mid+1] and L[mid]>L[mid-1]:
            return min(L[mid+1],L[mid-1])

        if L[mid]<L[mid+1] and L[mid]>L[mid-1]:
            return min(findMinInCircularList(L[:mid+1]),findMinInCircularList(L[mid:]))

print findMinInCircularList([38, 40, 55, 89, 2, 3, 6, 7, 13, 20, 23, 36])


def findMinInCircularList_loop(L):

    min_ = L[0]

    for e in L:
        if e<min_:
            min_ = e

    return min_

# def findMinInCircularList_iter(L):
 
#     cnt = len(L)
    
#     if cnt==1:
#     	return L[0]
#     elif cnt==2:
#     	return L[0] if L[0]<L[1] else L[1]
    
#     start = 0
#     end = cnt-1
    
#     while end>start+1:

#         mid = (end-start)//2

#         print L[mid-1],L[mid],L[mid+1]

#         if L[mid]<L[mid+1] and L[mid]<L[mid-1]:
#         	return L[mid]

#         if L[mid]<L[mid+1] and L[mid]>L[mid-1]:
#             end = mid

#         if L[mid]>L[mid+1] and L[mid]>L[mid-1]:
#             return min(L[mid+1],L[mid-1])

#     return max(start,end)

# print findMinInCircularList_iter([38, 40, 55, 89, 2, 3, 6, 7, 13, 20, 23, 36])
print findMinInCircularList_loop([38, 40, 55, 89, 2, 3, 6, 7, 13, 20, 23, 36])
