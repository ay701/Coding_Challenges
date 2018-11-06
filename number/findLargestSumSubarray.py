# Largest Sum Contiguous Subarray
# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
#
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Time Complexity: O(N)


def find_largest_sum_subarray(l):

    cur_max = l[0]
    max_ = l[0]

    for i in range(1, len(l)):
        cur_max = max(l[i], cur_max+l[i])

        if cur_max > max_:
            max_ = cur_max
            # print(i)

    return max_


l = [-2, -3, 4, -1, -2, 1, 5, -3]

print(find_largest_sum_subarray(l))
