# [LeetCode] Largest Number
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.

# convert each int to str and compare for each element if a+b > b+a


def largest_number(elements):

    result = str(elements[0])

    for element in elements[1:]:
        tmp_result = "".join(result)
        first = str(element) + tmp_result
        second = tmp_result + str(element)
        result = first if first > second else second

    return result


print(largest_number([3, 30, 34, 5, 9]))