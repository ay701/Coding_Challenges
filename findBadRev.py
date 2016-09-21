
# todo: write a function, int findFirstBadRev(int startRev, int endRev), which returns the first bad rev (x)
# given: boolean function, isBad(int rev), which returns true if the rev is bad
# base case: when to terminate the recursive function --> check to see if you're at the end (start >= end)
# optimization: if you find an element x that's bad but x-1 is good, then you can just return x-1
# http://www.code123.cc/docs/leetcode-notes/binary_search/first_bad_version.html

def findFirstBadRev(start,end):

    if end-start<0:
        return -1

    while start+1<end:
        mid = start+(end-start)//2

        if isbad(mid):
            end = mid
        else:
            start = mid

    if isbad(start):
        return start

    if isbad(end):
        return end

    return -1 

def isbad(n):
    if n in [96,97,98,99]:
        return True
  
    return False

print findFirstBadRev(0,100)
