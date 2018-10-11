# Given an object with an operator as a key and another object as a value,
# write a function that will perform the operator on the value.
# So you could be given something like {+,[1,2,3]} and your function would add the 3 values
# or you could be given something like {+,[1,2,{-,[1,2]}]} and have to recursively work.
# Use stack

import operator


def key_value_operator_cal(dic):

    if len(dic) < 1:
        return 0

    ops = {"+": operator.add, "-": operator.sub, "/": operator.div, "*": operator.mul}
    result = 0
    stack = [dic]
    cur_nums = []

    while stack:
        element = stack.pop()

        if isinstance(element, dict):
            stack.append(element.keys()[0])

            for x in element.values()[0]:
                stack.append(x)
        elif isinstance(element, int):
            cur_nums.append(element)
        elif element in ["+", "-", "*", "/"]:
            cur_nums = cur_nums[::-1]
            tmp_result = cur_nums[0]

            for x in cur_nums[1:]:
                tmp_result = ops[element](tmp_result, x)

            result = tmp_result
            cur_nums = [tmp_result]

    return result


dic_1 = {"+": [1, 2, 3]}
dic_2 = {"+": [1, 2, {"-": [1, 2]}]}

print key_value_operator_cal(dic_2)
