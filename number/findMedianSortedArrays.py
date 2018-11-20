# Median: In probability theory and statistics, a median is described as the number
# separating the higher half of a sample,
# a population, or a probability distribution, from the lower half.
# The median of a finite list of numbers can be found by arranging all the numbers from lowest value to highest value 
# and picking the middle one.
# For getting the median of input array { 12, 11, 15, 10, 20 }, first sort the array. 
# We get { 10, 11, 12, 15, 20 } after sorting. Median is the middle element of the sorted array which is 12.
#
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
# Time complexity Log(n)
# Divide Conquer


def find_median_sorted_arrays(l1, l2):

    n1 = len(l1)
    n2 = len(l2)

    if n1 == 1 and n2 == 1:
        return (l1[0]+l2[0]) // 2

    if n1 == 2 and n2 == 2:
        return (min(l1[0], l2[0])+max(l1[1], l2[1])) // 2

    m1 = n1//2
    m2 = n2//2

    m1_val = (l1[m1] + l1[m1-1])//2 if n1 % 2 == 0 else l1[m1]
    m2_val = (l2[m2] + l2[m2-1])//2 if n2 % 2 == 0 else l2[m2]

    if m1_val == m2_val:
        return m1
    elif m1_val > m2_val:
        small = l2[m2:n2]
        large = l1[0:m1+1]

        # print small, big
        return find_median_sorted_arrays(small, large)
    else:
        small = l1[m1:n1]
        large = l2[0:m2+1]

        # print small, big
        return find_median_sorted_arrays(small, large)

print find_median_sorted_arrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])
# print find_median_sorted_arrays([1, 2, 3, 6], [4, 6, 8, 10])
# print find_median_sorted_arrays([1, 4], [2, 3])


# Write code to parse urls into a sitemap tree structure and display it as text. For example, the following urls will result in this printed structure.

# Milestones:
# 1. Parse routes into data structure
# 2. Print data structure as simply as possible to check parsing
# 3. Format text output like shown in below

# [
#     '/home/anti-depressants/xanax',
#     '/home/heart/lipitor',
#     '/home/heart/atorvastatin',
#     '/home/heart/lipitor',
#     '/home/heart/heart',
#     '/drugs/nasal/flonase',
#     '/drugs/topical',
#     '/drugs/routes/oral/tablets',
#     '/drugs/routes/nasal/flonase',
# ]

# - home
#     - anti-depressants
#         - xanax
#     - heart
#         - lipitor
#         - atorvastatin
#         - heart
# - drugs
#     - nasal
#         - flonase
#     - topical
#     - routes
#         - oral
#             - tablets
#         - nasal
#             - flonase



