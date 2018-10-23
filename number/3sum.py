# Find a triplet that sum to a given value
# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
# If there is such a triplet present in array, then print the triplet and return true. Else return false.
# For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
# then there is a triplet (12, 3 and 9) present in array whose sum is 24.

# First Solution
# O(N)


def three_sum(l, sum):

    output = []
    n = len(l)
    dic = {}

    for i in range(n-2):
        cur_sum = sum - l[i]

        for j in range(i+1, n):
            k = cur_sum - l[j]

            if dic.get(k) and l[i] != k and l[j] != k:
                output.append((l[i], l[j], k))
            else:
                dic[l[j]] = True

    return output


print(three_sum([1, 4, 45, 6, 10, 8], 22))


# Second Solution
# O(N*2)
# Sort the input then

def three_sum2(l, sum):
    output = []
    l.sort()
    n = len(l)

    print(l)

    for i in range(n-2):

        left = i + 1
        right = n - 1

        while left < right:
            if l[left] + l[right] + l[i] == sum:
                output.append((l[i], l[left], l[right]))
                left += 1
            elif l[left] + l[right] + l[i] > sum:
                right -= 1
            else:
                left += 1

    return output

print(three_sum2([1, 4, 45, 6, 10, 8], 22))
