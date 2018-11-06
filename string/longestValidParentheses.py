# LeetCode - Longest Valid Parentheses (Java)
#
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
# Analysis
#
# This problem is similar with Valid Parentheses, which can be solved by using a stack.


def longest_valid_parenthesis(input):

    stack = []
    result = ""

    for curr, s in enumerate(input):
        if s == "(":
            stack.append(curr)
        else:
            if len(stack) == 0:
                continue

            last = stack.pop()

            if curr-last > len(result):
                result = input[last:curr+1]

    return result


print(longest_valid_parenthesis("()))"))

