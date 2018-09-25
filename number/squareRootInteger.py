# Liner approach by increasing number from 0, 1 ...
# Until the result is larger than number, exit
# Time complexity : N

def squareRootInteger(x):
    if x in [0,1]:
        return x

    i = 1
    result = 1
    while result<=x:
        i += 1
        result = i*i

    return i-1

print(squareRootInteger(109))

# Use binary search
# Time complexity : LogN

def squareRootInteger2(x):
    if x in [0,1]:
        return x

    start = 1
    end = x
    result = 1

    while start<=end:
        mid = (start+end)//2

        # Perfect match
        if mid*mid==x:
            return mid

        if mid*mid<x:
            start = mid+1
            result = mid
        else:
            end = mid-1

    return result

print(squareRootInteger2(109))
