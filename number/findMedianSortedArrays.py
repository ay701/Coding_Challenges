# Median: In probability theory and statistics, a median is described as the number separating the higher half of a sample, 
# a population, or a probability distribution, from the lower half.
# The median of a finite list of numbers can be found by arranging all the numbers from lowest value to highest value 
# and picking the middle one.
# For getting the median of input array { 12, 11, 15, 10, 20 }, first sort the array. 
# We get { 10, 11, 12, 15, 20 } after sorting. Median is the middle element of the sorted array which is 12.
# Time complexity Log(n)


def find_median_sorted_arrays(l1, l2):

    m1 = len(l1)/2
    m2 = len(l2)/2

    print m1, m2

    if len(l1) == 0:
        return l2[m2]

    if len(l2) == 0:
        return l1[m1]

    if l1[m1] == l2[m2]:
        return l1[m1]

    if len(l1) == 2 and len(l2) == 2:
        return (max(l1[0], l2[0]) + min(l1[1], l2[1]))/2

    if l1[m1] > l2[m2]:
        small = l2[m2:len(l2)]
        big = l1[0:m1+1]
        #print small, big
        return find_median_sorted_arrays(small, big)
    elif l1[m1] < l2[m2]:
        small = l1[m1:len(l1)]
        big = l2[0:m2+1]
        # print small, big
        return find_median_sorted_arrays(small, big)

print find_median_sorted_arrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])




