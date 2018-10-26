# LeetCode - Search Insert Position
#
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
#
# Here are few examples.
#
#
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0

# Binary Search Problem


def search_insert_position(l, target):

    left = 0
    right = len(l)

    while left <= right:
        mid = (left+right)//2

        if l[mid] < target:
            left = mid
        elif l[mid] > target:
            right = mid
        else:
            return mid

    return right

print(search_insert_position([1, 3, 5, 6], 5))

