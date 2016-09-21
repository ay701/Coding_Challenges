# @param num, a list of integer
# @return an integer
# this only find one peak number

def findPeakElement(nums):
    start = 0
    end = len(nums)-1

    while start+1 < end:
        mid = (start+end)//2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
            
        if nums[mid] < nums[mid+1]:
            start = mid+1
        else:
            end = mid-1

    return start if nums[start]>=nums[end] else end

# return 1
print findPeakElement([2,3,17,5,16,8,1])
# return 0
print findPeakElement([4,3,1])
