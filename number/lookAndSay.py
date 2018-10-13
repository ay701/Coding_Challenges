# Look-and-Say Sequence
# Find the nth term in Look-and-say (Or Count and Say) Sequence.
# The look-and-say sequence is the sequence of below integers:
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
#
# How to find nth term?
# Example:
#
# Input: n = 3
# Output: 21
#
# Input: n = 5
# Output: 111221

import collections


def look_and_say(n):

    if n == 1:
        return 1

    prev = str(1)

    for i in range(1, n):
        output = ""
        cnt = len(prev)
        start = 0
        end = 0
        dic = collections.defaultdict(int)

        while end < cnt:
            end += 1

            if prev[end-1] != prev[start]:
                output += str(dic[prev[start]]) + prev[start]
                del dic[prev[start]]
                start = end-1

            dic[str(prev[start])] += 1

        print(dic)

        for k, v in dic.iteritems():
            output += str(v) + k

        print(prev)
        prev = output

    return prev

print(look_and_say(6))
