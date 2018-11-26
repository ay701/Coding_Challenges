# [LeetCode] Compare Version Numbers
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1;
# if version1 <version2 return -1;
# otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Example 1:
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Example 2:
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# Example 3:
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


def compare_versions(v1, v2):

    v_1 = v1.split(".")
    v_2 = v2.split(".")

    m = len(v_1)
    n = len(v_2)

    print(v_1, v_2)

    if m < n:
        for _ in range(m-n):
            v_1.append("0")
    elif m > n:
        for _ in range(m-n):
            v_2.append("0")

    print(v_1, v_2)

    for i in range(len(v_1)):
        if int(v_1[i]) > int(v_2[i]):
            return 1
        elif int(v_1[i]) < int(v_2[i]):
            return -1

    return 0


v1 = "0.1"
v2 = "1.1"

v1 = "1.0.1"
v2 = "1"
#
# v1 = "7.5.2.4"
# v2 = "7.5.3"

print(compare_versions(v1, v2))
