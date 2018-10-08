# todo: write a function, int findFirstBadRev(int startRev, int endRev), which returns the first bad rev (x)
# given: boolean function, isBad(int rev), which returns true if the rev is bad
# base case: when to terminate the recursive function --> check to see if you're at the end (start >= end)
# optimization: if you find an element x that's bad but x-1 is good, then you can just return x-1
# http://www.code123.cc/docs/leetcode-notes/binary_search/first_bad_version.html


def first_bad_rev(start, end):

    if end - start < 0:
        return -1

    while start+1 < end:
        mid = start + (end-start)//2

        if is_bad(mid):
            end = mid
        else:
            start = mid

    if is_bad(start):
        return start

    if is_bad(end):
        return end

    return -1 


def is_bad(n):
    if n in [96, 97, 98, 99]:
        return True
  
    return False

print first_bad_rev(0, 100)


def first_bad_rev_2(start, end):

    if start > end:
        return -1
    elif start == end:
        return start if is_bad(start) else -1
    elif end - start == 1:
        if is_bad(start):
            return start
        elif is_bad(end):
            return end

    mid = start + (end - start) // 2

    if is_bad(mid):
        return first_bad_rev_2(start, mid)
    else:
        return first_bad_rev_2(mid, end)

    return -1

print first_bad_rev_2(0, 100)
