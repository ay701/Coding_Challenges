# -*- coding: utf-8 -*-
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
#
# Dynamic Programming
# Time complexity is O(1)
# Only use cur_sum and max_ to store values


def maximum_sub_array(L):

    max_ = L[0]
    cur_sum = L[0]

    for item in L[1:]:

        cur_sum = max(cur_sum+item, item)
        max_ = max(cur_sum, max_)
        #print cur_sum, max_

    return max_

# L = [2,3,4,0,-1]
L = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# L = [−2,1,−3,4,−1,2,1,−5,4]
print maximum_sub_array(L)