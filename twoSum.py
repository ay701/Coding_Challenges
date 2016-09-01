#Given an array of integers, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution.
#Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2

def two_sum(arr,targ):
    look_for = {}
    for n,x in enumerate(arr):
        try:
            #print n, x
            return look_for[x] + 1, n + 1
        except KeyError:
            print n, x
            look_for.setdefault(targ - x,n)
            print look_for

a = (2,7,1,15)
t = 9
print(two_sum(a,t))
# (1,2)
