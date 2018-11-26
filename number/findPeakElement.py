# Given an array of integers. Find a peak element in it. 
# An array element is peak if it is NOT smaller than its neighbors. 
# For corner elements, we need to consider only one neighbor. 
# For example, for input array {5, 10, 20, 15}, 20 is the only peak element. 
# For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90. 
# Note that we need to return any one peak element.

# Following corner cases give better idea about the problem.
# 1) If input array is sorted in strictly increasing order, the last element is always a peak element. 
# For example, 50 is peak element in {10, 20, 30, 40, 50}.
# 2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 
# 100 is the peak element in {100, 80, 60, 50, 20}.
# 3) If all elements of input array are same, every element is a peak element.

# It is clear from above examples that there is always a peak element in input array in any input array.
# @param num, a list of integer
# @return an integer
# this is only to find one peak number


def find_peak_element(nums):

    n = len(nums)

    if n == 1:
        return nums

    left = 0
    right = n-1

    while left < right:
        mid = left + (right-left)//2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return nums[mid]
        elif nums[mid] < nums[mid-1]:
            right = mid
        elif nums[mid] < nums[mid+1]:
            left = mid

    return nums[mid]


print find_peak_element([2, 3, 17, 5, 16, 8, 1])
print find_peak_element([4, 3, 1])
print find_peak_element([1, 3, 20, 4, 1, 0])
