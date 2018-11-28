# Use Reservoir Sampling
# We are given a big array (or stream) of numbers (to simplify),
# and we need to write an efficient function to randomly select k numbers where 1 <= k <= n.
# Let the input array be stream[].

# 1) Create an array reservoir[0..k-1] and copy first k items of stream[] to it.
# 2) Now one by one consider all items from (k+1)th item to nth item.
#  a) Generate a random number from 0 to i where i is index of current item in stream[].
#     Let the generated random number is j.
#  b) If j is in range 0 to k-1, replace reservoir[j] with arr[i]


import random


def random_select_k_elements(elements, k):

    n = len(elements)

    if n < k:
        raise Exception('Too small')

    if n == k:
        return elements

    reservoir = elements[0:k]

    i = k

    while i < n:
        j = random.randrange(i+1)

        if j < k:
            reservoir[j] = elements[i]

        i += 1

    return reservoir

stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(random_select_k_elements(stream, 5))

