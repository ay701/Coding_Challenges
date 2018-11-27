# [LeetCode] Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
# Note:
# -The length of both num1 and num2 is < 110.
# -Both num1 and num2 contains only digits 0-9.
# -Both num1 and num2 does not contain any leading zero.
# -You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#     3 2 1
# x     4 3
# _________
#     9 6 3
# 1 2 8 4
# _________
# 1 3 8 0 3

import math


def multiply_strings(s1, s2):

    # Put each position's multiplication into array
    nums = []

    for c2 in reversed(s2):
        pos, flag, num = 0, 0, 0

        for c1 in reversed(s1):
            tmp = int(c1) * int(c2) + flag

            if tmp // 10 == 1:
                tmp %= 10
                flag = 1

            num += tmp * math.pow(10, pos)
            pos += 1

        num += math.pow(10, pos) if flag == 1 else 0
        nums.append(int(num))

    return sum([int(math.pow(10, i)*e) for i, e in enumerate(nums)])


print(multiply_strings("321", "43"))

