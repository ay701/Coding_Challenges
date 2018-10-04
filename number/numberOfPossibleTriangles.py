# Given an unsorted array of positive integers.
# Find the number of triangles that can be formed with three different array elements as three sides of triangles.
# For a triangle to be possible from 3 values, the sum of any two values (or sides) must be greater than the third value (or third side).
# For example, if the input array is {4, 6, 3, 7}, the output should be 3.
# There are three triangles possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. Note that {3, 4, 7} is not a possible triangle.
# As another example, consider the array {10, 21, 22, 100, 101, 200, 300}.
# There can be 6 possible triangles: {10, 21, 22}, {21, 100, 101}, {22, 100, 101}, {10, 100, 101}, {100, 101, 200} and {101, 200, 300}


def num_of_possible_triangles(l):

    output = []
    length = len(l)

    if length < 3:
        return []

    for i in range(0, length):
        for j in range(i+1, length):
            for k in range(j+1, length):

                borders = [l[i], l[j], l[k]]
                cnt = 0

                for x in range(3):
                    sum_ = sum([border for border in borders if border != borders[x]])

                    if borders[x] < sum_:
                        cnt += 1

                if cnt == 3:
                    output.append(borders)

    return output


# Driver function to test above function
# Time Complexity: O(N^3) where N is the size of input array.
arr = [10, 21, 22, 100, 101, 200, 300]
print(num_of_possible_triangles(arr))


def num_of_possible_triangles_2(l):
    length = len(l)

    if length < 3:
        return 0

    quick_sort(l)

    i = 0
    j = 1
    cnt = 0

    while i < length-2:
        k = j+1

        while k < length and l[i]+l[j] > l[k]:
            k += 1

        cnt += k - j - 1

        j += 1

        if j >= length:
            i += 1
            j = i+1

    return cnt

# Driver function to test above function
# Time Complexity: O(N^2) where N is the size of input array.
arr = [10, 21, 22, 100, 101, 200, 300]
print(num_of_possible_triangles_2(arr))