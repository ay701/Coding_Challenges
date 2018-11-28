# LeetCode - Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.
#
# Typical bucket sort problem: Use count of frequency as bucket key, list of elements as value
# https://www.youtube.com/watch?v=EYFcQRwcqk0


from collections import defaultdict


def top_k_frequent_elements(elements, n):

    dic = defaultdict(int)
    result = []

    for element in elements:
        dic[element] += 1

    # Create K+1 size bucket
    bucket = [[] for _ in range(len(elements)+1)]

    # Fill in bucket
    for k, v in dic.items():
        bucket[v].append(k)

    print(bucket)

    # backward traverse bucket
    for elements in bucket[::-1]:
        for element in elements:
            result.append(element)
            print(result, len(result), n)

            if n == len(result):
                return result

    return []

print(top_k_frequent_elements([1, 2, 2, 3, 3, 3, 5, 5, 5, 6, 4], 2))

# Time Complexity: O(N)  -> O(N+N+N)
# Space Complexity: O(N)  -> Bucket Size + Dictionary Size

