# Leetcode - 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
#
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

# Time Complexity: O(NlogN)
# Use Binary Tree Search
def find_only_duplicates(nums):

    n = len(nums)

    if n == 0:
        raise Exception('Input cannot be empty.')

    if n == 1:
        raise Exception('One element list has no duplicate.')

    left = 1
    right = n

    while left < right:
        mid = left + (right-left) // 2
        cnt = 0

        for num in nums:
            if num <= mid:
                cnt += 1

        if cnt <= mid:
            left = mid+1
        else:
            right = mid

    return left


# print(find_only_duplicates([3, 1, 3, 4, 2]))


# Time Complexity: O(NlogN)
# Space complexity: O(1)
# Use Linked list cycle
# NEED TO VERIFY --- THIS APPROACH


def find_only_duplicates_(nums):

    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        print(slow, fast)

        if slow == fast:
            break

    fast = 0

    while slow != fast:
        print(slow, fast)
        slow = nums[slow]
        fast = nums[fast]

    return slow


print(find_only_duplicates_([3, 1, 3, 4, 2]))