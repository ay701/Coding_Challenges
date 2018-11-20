#
# Flatten a multi dimension array
# Use iterative approach and recursive
#

import itertools

# flattened_list = list(itertools.chain([[1], [2, 3], [4, [5, [6, [7, [8]]]]]]))
# print(flattened_list)


def iter_flatten(L):
    return [item for sub_l in L for item in sub_l]


def recur_flatten(L):
    if L is []:
        return L

    if isinstance(L[0], list):
        return recur_flatten(L[0]) + recur_flatten(L[1:])

    return L[:1] + recur_flatten(L[1:])


def recur_flatten_2(L):
    if isinstance(L, list):
        if len(L) == 0:
            return []
        return recur_flatten_2(L[0]) + recur_flatten_2(L[1:])
    else:
        return [L]


####################
# Button Interview #
####################

def flatten(l, func_seq):

    if l is []:
        return l

    output = []
    queue = l
    dic = {1: 'even_func', 2: 'odd_func'}

    while len(queue) > 0:
        e = queue.pop(0)

        if e is None:
            continue
        elif isinstance(e, list):
            queue = e + queue
            continue
        elif isinstance(e, int):
            output.append(e)
            continue
        else:
            raise Exception('Invalid element {}', format(element))

    return map(output, dic[func_seq])


def even_func(arr):
    return [element for element in arr if element % 2 == 0]

# print iter_flatten([[1], [2, 3], [4, [5, [6, [7, [8]]]]]])
# print recur_flatten([[1], [2, 3], [4, [5, [6, [7, [8]]]]]])
# print recur_flatten_2([[1], [2, 3], [4, [5, [6, [7, [8]]]]]])

print(flatten([[1], [2, 3], [4, [5, [6, [7, [8]]]]]]))
print(flatten([]))
print(flatten([-1, "xxx"]))
print(flatten([[None, 1], [None, None]]))
print(flatten([[None, 1], [None], [None]]))
print(flatten([6, 2, [1, [9, 3], None], 2]))
print(flatten([6, 2, [1, [9, 3], None, None], 2]))
print(flatten([6, 2, [1, [9, 3], None], 2]))

