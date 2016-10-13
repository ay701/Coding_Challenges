# Median: In probability theory and statistics, a median is described as the number separating the higher half of a sample, 
# a population, or a probability distribution, from the lower half.
# The median of a finite list of numbers can be found by arranging all the numbers from lowest value to highest value 
# and picking the middle one.
# For getting the median of input array { 12, 11, 15, 10, 20 }, first sort the array. 
# We get { 10, 11, 12, 15, 20 } after sorting. Median is the middle element of the sorted array which is 12.

def findMedianSortedArrays(L1,L2):

    m1 = len(L1)/2
    m2 = len(L2)/2

    print m1,m2

    if len(L1)==0 :
    	return m2

    if len(L2)==0 :
    	return m1

    if L1[m1]==L2[m2]:
    	return L1[m1]

    if len(L1)==2 and len(L2)==2:
    	return (max(L1[0],L2[0])+min(L1[1],L2[1]))/2

    if L1[m1]>L2[m2]:
    	small = L2[m2:len(L2)]
    	big = L1[0:m1+1]
    	#print small, big
    	return findMedianSortedArrays(small,big)
    elif L1[m1]<L2[m2]:
        small = L1[m1:len(L1)]
        big = L2[0:m2+1]
    	# print small, big
    	return findMedianSortedArrays(small,big)

print findMedianSortedArrays([1, 12, 15, 26, 38],[2, 13, 17, 30, 45])




