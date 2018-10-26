# Problem:

# Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


def insert_interval(intervals, new_interval):

    output = []
    n = len(intervals)

    for i in range(n):

		if intervals[i][0] > new_interval[1]:
			output.append(new_interval)
			output.extend(intervals[i:])
			return output

		if intervals[i][1] < new_interval[0]:
			output.append(intervals[i])
			continue

		first = min(new_interval[0], intervals[i][0])
		second = max(new_interval[1], intervals[i][1])
		new_interval = [first, second]

	return output.append(new_interval)


L = [[1,2],[3,5],[6,7],[8,10],[12,16]]
interval_ = [4,9]
# interval = [-1,0]
# interval = [2,3]
print insert_interval(L, interval_)


