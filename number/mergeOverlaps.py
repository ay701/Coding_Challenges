# Merge and Sort overlapping segments
#
# A segment has a 'start' and an 'end' where 'start' >= 0 and 'end' > 'start'.
# A segment overlaps another segment even if their boundaries are the same.
# Given a list of unordered segments, write a function that merges all the overlapping segments and sorts them by 'start'.
#
# segments = [
#     { 'start': 10, 'end': 16 },
#     { 'start': 17, 'end': 18 },
#     { 'start': 1, 'end': 2 },
#     { 'start': 8, 'end': 10 },
#     { 'start': 17, 'end': 20 },
#     { 'start': 19, 'end': 25 }
# ]
#
# print merge_and_sort(segments)
#
# [
#     { 'start': 1, 'end': 2 },
#     { 'start': 8, 'end': 16 },
#     { 'start': 17, 'end': 25 }
# ]
#
# Merge and Sort overlapping segments
#
# A segment has a 'start' and an 'end' where 'start' >= 0 and 'end' > 'start'.
# A segment overlaps another segment even if their boundaries are the same.
# Given a list of unordered segments, write a function that merges all the overlapping segments and sorts them by 'start'.
#
# segments = [
#     { 'start': 10, 'end': 16 },
#     { 'start': 17, 'end': 18 },
#     { 'start': 1, 'end': 2 },
#     { 'start': 8, 'end': 10 },
#     { 'start': 17, 'end': 20 },
#     { 'start': 19, 'end': 25 }
# ]
#
# print merge_and_sort(segme nts)
#
# [
#     { 'start': 1, 'end': 2 },
#     { 'start': 8, 'end': 16 },
#     { 'start': 17, 'end': 25 }
# ]
#

segments = [
    {'start': 10, 'end': 16},
    {'start': 17, 'end': 18},
    {'start': 1, 'end': 2},
    {'start': 8, 'end': 10},
    {'start': 17, 'end': 20},
    {'start': 19, 'end': 25},
    {'start': 24, 'end': 27}
]


def merge_overlaps(segments):
    output = []
    
    sorted_segs = sorted(segments)
    
    if len(sorted_segs) <= 1:
        return sorted_segs

    print sorted_segs
    cur = sorted_segs[0]

    for i in range(1, len(sorted_segs)):
 
        nex = sorted_segs[i]

        if cur["end"] < nex["start"]:
            output.append(cur)
            cur = nex
        else:
            cur["end"] = nex["end"]

    output.append(cur)
        
    return output

print merge_overlaps(segments)
