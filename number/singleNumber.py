# Given an array of integers, every element appears twice except for one.
# Find that single one.
# Input: 3, 3, 2, 4, 4, 5, 5
# Middle output: 0, 2, 6, 2, 7, 2


def single_number(l):

    ans = l[0]

    for i in range(1, len(l)):
        ans ^= l[i]
        print(l[i], ans)

    return ans

L = [3, 3, 2, 4, 4, 5, 5]
print(single_number(L))
