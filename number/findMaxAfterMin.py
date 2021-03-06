# [10,1,15,2,3,5,1,3]


def find_max_after_min(l):

    if len(l) <= 1:
        return None

    prev = l[0]
    min_ = prev
    max_ = None

    for cur in l[1:]:

        if prev < min_:
            min_ = prev
            max_ = cur if cur > prev else None
        elif cur == min_:
            if max_ is None or cur > max_:
                max_ = cur

        prev = cur
 
    return max_

print find_max_after_min([10, 1, 15, 2, 3, 5, 1, 3, 10, 1, 16, 2, 3, 5, 1, 3])

