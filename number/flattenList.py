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
    if L == []:
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

print iter_flatten([[1], [2, 3], [4, [5, [6, [7, [8]]]]]])
print recur_flatten([[1], [2, 3], [4, [5, [6, [7, [8]]]]]])
print recur_flatten_2([[1], [2, 3], [4, [5, [6, [7, [8]]]]]])
