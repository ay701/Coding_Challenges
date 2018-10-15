# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# use first string as base, a pointer to compare


def longest_common_prefix(sts):

    n = len(sts[0])

    for i in range(n):
        for st in sts:
            if len(st) <= i or st[i] != sts[0][i]:
                return sts[0][:i]

    return sts[0]

sts = ["hello", "heabc", "hell"]
print(longest_common_prefix(sts))
