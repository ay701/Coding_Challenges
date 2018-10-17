# Find if there is a subarray with 0 sum
# Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.
# Examples :
#
# Input: {4, 2, -3, 1, 6}
# Output: true
# There is a subarray with zero sum from index 1 to 3.
#
# Input: {4, 2, 0, 1, 6}
# Output: true
# There is a subarray with zero sum from index 2 to 2.
#
# Input: {-3, 2, 3, 1, 6}
# Output: false
# There is no subarray with zero sum.

# https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

# Note:
# We can also use hashing.
# The idea is to iterate through the array and for every element arr[i],
# calculate sum of elements form 0 to i (this can simply be done as sum += arr[i]).
# If the current sum has been seen before, then there is a zero sum array.
# Hashing is used to store the sum values, so that we can quickly store sum
# and find out whether the current sum is seen before or not.


def find_zero_sum_subarray(l):

    n = len(l)

    if n == 1:
        return True if l[0] == 0 else False

    hash_map = {l[0]: 0}

    for i in range(1, n):
        tmp = hash_map.keys()[-1] + l[i]

        print hash_map

        if hash_map.get(tmp):
            return True
        else:
            hash_map[tmp] = i

    return False


l = [1, 3, 2, -1, 5]
print(find_zero_sum_subarray(l))
