# LeetCode - Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.
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
    for elements in reversed(bucket):
        for element in elements:
            result.append(element)
            print(result, len(result), n)

            if n == len(result):
                return result

    return []

print(top_k_frequent_elements([1,2,2,3,3,3,5,5,5,6,4], 2))