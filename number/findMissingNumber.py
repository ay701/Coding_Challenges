def find_missing_number(l):

    n = len(l)

    x1 = l[0]
    x2 = 1

    for e in l[1:]:
        x1 = x1 ^ e

    for i in range(2, n+2):
        x2 = x2 ^ i

    return x1 ^ x2

print find_missing_number([1, 2, 3, 4, 5, 7, 8, 9, 10])


# Get sum of all number
# Deduct element one by one, to get the missing one


def find_missing_number_2(l):

    n = len(l)

    sum_ = (n+1)*(n+2)//2

    for e in l:
        sum_ -= e

    return sum_

print find_missing_number_2([1, 2, 3, 4, 5, 7, 8, 9, 10])
