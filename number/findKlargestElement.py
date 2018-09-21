# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
# O(n)

def findKlargestElement(L,k):

    pivot = L[-1]
    small_list, large_list = [], []

    for element in L:
    	if element<pivot:
    		small_list.append(element)
    	elif element>pivot:
    		large_list.append(element)

    print small_list, large_list

    if k<=len(large_list):
    	return findKlargestElement(large_list,k)
    elif k>len(L)-len(small_list):
    	return findKlargestElement(small_list,k-(len(L)-len(small_list)))
    
    return pivot

print findKlargestElement([3,2,1,5,6,4],2)

