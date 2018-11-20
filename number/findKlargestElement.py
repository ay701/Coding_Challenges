# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 <= k <= array's length.

# http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
# O(n)

# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

# For first K smallest element :
# Use MaxHeap for first 0, K-1 element from array
# Then, next K to N-1 element : if its less than root, swap & heapify

# For first K largest element :
# Use MinHeap for first 0, K-1 element from array
# Then, next K to N-1 element : if its larger than root, swap & heapify
# Time complexity of this solution is O(k + (n-k)*Logk)

# https://www.programcreek.com/2014/05/leetcode-kth-largest-element-in-an-array-java/
# We can use a min heap to solve this problem. The heap stores the top k elements.
# Whenever the size is greater than k, delete the min.
# Time complexity is O(nlog(k)). Space complexity is O(k) for storing the top k numbers.


def find_k_largest_element(l, k):

    pivot = l[-1]
    small_list, large_list = [], []

    for element in l:
        if element < pivot:
            small_list.append(element)
        elif element > pivot:
            large_list.append(element)

    print small_list, large_list

    if k <= len(large_list):
        return find_k_largest_element(large_list, k)
    elif k > len(l)-len(small_list):
        return find_k_largest_element(small_list, k-(len(l)-len(small_list)))
    
    return pivot

# print find_k_largest_element([3, 2, 1, 5, 6, 4], 2)


# Use Min heap

# Python code to demonstrate working of
# heapify(), heappush() and heappop()
# importing "heapq" to implement heap queue

import heapq

# initializing list
# li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
# heapq.heapify(li)

# printing created heap
# print ("The created heap is : ")
# print (list(li))


def find_k_largest_element(l, k):

    n = len(l)
    heap = l[0:k]

    # min heap -> heap[0] is always the smallest
    heapq.heapify(heap)

    for i in range(k, n):
        heap[0] = l[i] if l[i] > heap[0] else heap[0]
        heapq.heapify(heap)
        print(heap)

    return heapq.heappop(heap)

print(find_k_largest_element([3, 2, 1, 5, 6, 4], 2))
# print(find_k_largest_element([3, 2, 1, 5, 6, 4], 5))

