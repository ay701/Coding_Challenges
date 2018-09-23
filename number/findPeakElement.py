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

def findPeakElement(nums):
    start = 0
    end = len(nums)-1

    while start+1 < end:
        mid = (start+end)//2
        
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return nums[mid]
            
        if nums[mid] < nums[mid+1]:
            start = mid+1
        else:
            end = mid-1

    return nums[start] if nums[start]>=nums[end] else nums[end]

print findPeakElement([2,3,17,5,16,8,1])
print findPeakElement([4,3,1])
print findPeakElement([1, 3, 20, 4, 1, 0])

# def findPeakElements(nums):
#     peaks = []

#     length = len(nums)
#     start = 0
#     end = length-1

#     # if length==1:
#     #     return [nums[0]]

#     # if length==2:
#     #     return [nums[0]] if nums[0]>=nums[1] else [nums[1]]

#     # if length==3 and nums[1]>nums[0] and nums[1]>nums[2]:
#     #     return [nums[1]]

#     while start+1<end:

#         mid = (start+end)//2

#         if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
#             peaks.append(nums[mid])
#             print mid+1, end
#             # print nums[mid+1:end]
#             peaks += findPeakElements(nums[start:mid+1])
#             peaks += findPeakElements(nums[mid:end])

#         if nums[mid]<nums[mid-1]:
#             end = mid-1
#         else:
#             start = mid+1

#     return peaks+[nums[start]] if nums[start]>=nums[end] else peaks+[nums[end]]

# print findPeakElements([2,3,17,5,16,8])