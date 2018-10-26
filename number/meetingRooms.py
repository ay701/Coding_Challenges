# LeetCode - Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings. For example, Given [[0, 30],[5, 10],[15, 20]], return false.


def merge_sort(l):

    # merge_sort
    n = len(l)

    if n < 2:
        return l

    mid = n//2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    i, j = 0, 0
    output = []

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    while i < len(left):
        output.append(left[i])
        i += 1

    while j < len(right):
        output.append(right[j])
        j += 1

    return output


def meeting_rooms(times):

    n = len(times)

    if n < 2:
        return True

    times = merge_sort(times)
    prev = times[0]

    for cur in times[1:]:
        if prev[0] == cur[0] or prev[1] > cur[0]:
            return False

        prev = cur

    return True

print(meeting_rooms([[0, 30], [31, 40], [50, 120]]))
# print(meeting_rooms([[0, 30], [5, 10], [15, 20]]))
