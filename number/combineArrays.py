# Combine two arrays, with sorted order
# Without duplicated elements


def combine_arrays(l1, l2):
  
    l = l1 + l2

    if len(l) < 2:
        return l

    l = merge_sort(l)

    cur = l[0]
    output = [cur]

    for i, nex in enumerate(l[1:]):
        if cur == nex:
            continue

        cur = nex        
        output.append(cur)

    return output


def merge_sort(l):

    mid = int(len(l)/2)

    if len(l) < 2:
        return l

    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    i = 0
    j = 0
    output = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output += left[i:]+right[j:]

    return output

l1 = [1, 4, 5, 6, 10, 5, 8]
l2 = [1, 14, 3, 16, 11, 15, 8]

print combine_arrays(l1, l2)


# Use list comprehension
# But this will not remove duplicates from individual list
def combine_arrays1(l1, l2):

    output = l1
    output.extend([x for x in l2 if x not in output])
    return output

print combine_arrays1(l1, l2)


# Use set
def combine_arrays2(l1, l2):

    s1 = set(l1)
    s2 = set(l2)

    return list(s2) + list(s1 - s2)

print combine_arrays2(l1, l2)

