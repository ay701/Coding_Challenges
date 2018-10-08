# You are given a list of numbers.
# When you reach the end of the list you will come back to the beginning of the list (a circular list).
# Write the most efficient algorithm to find the minimum # in this list. 
# Find any given # in the list.
# The numbers in the list are always increasing but you don't know where the circular list begins,
# ie: 38, 40, 55, 89, 6, 13, 20, 23, 36.


def find_min_in_circular_list(l):
 
    n = len(l)
    
    if n == 1:
        return l[0]

    if n == 2:
        return l[0] if l[0] < l[1] else l[1]

    mid = n//2

    print l[mid-1], l[mid], l[mid+1]

    if l[mid] < l[mid+1] and l[mid] < l[mid-1]:
        return l[mid]

    if l[mid] > l[mid+1] and l[mid] > l[mid-1]:
        return min(l[mid+1], l[mid-1])

    if l[mid] < l[mid+1] and l[mid] > l[mid-1]:
        return min(find_min_in_circular_list(l[:mid+1]), find_min_in_circular_list(l[mid:]))

print find_min_in_circular_list([38, 40, 55, 89, 2, 3, 6, 7, 13, 20, 23, 36])


def find_min_in_circular_list_iter(l):
    n = len(l)

    if n == 1:
        return l[0]

    if n == 2:
        return l[0] if l[0] < l[1] else l[1]

    start = 0
    end = n

    while start <= end:

        mid = (end-start)//2

        print(l[mid-1], l[mid], l[mid+1])

        if l[mid-1] > l[mid] and l[mid] < l[mid+1]:
            return l[mid]

        if l[mid-1] < l[mid] and l[mid+1] < l[mid]:
            return min(l[mid-1], l[mid+1])

        end = mid+1

    return start if start > end else end


print find_min_in_circular_list_iter([38, 40, 55, 89, 2, 3, 6, 7, 13, 20, 23, 36])
