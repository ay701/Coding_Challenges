# Problem:

# Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

def insertInterval(intervals, new_interval):
     
    output = []
    insert_pos = 0
          
    for interval in intervals:
    	if interval[0]>new_interval[1]:
    		output.append(interval)
    	elif interval[1]<new_interval[0]:
    		output.append(interval)
    		insert_pos += 1
    	else:
    		new_interval = [min(new_interval[0], interval[0]), max(new_interval[1],interval[1])]

    output.insert(insert_pos, new_interval)

    return output

L = [[1,2],[3,5],[6,7],[8,10],[12,16]]
interval = [4,9]
# interval = [-1,0]
# interval = [2,3]
print insertInterval(L, interval)


