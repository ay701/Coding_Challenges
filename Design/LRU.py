# LRU Cache Implementation
# How to implement LRU caching scheme? What data structures should be used?
# We are given total possible page numbers that can be referred.
# We are also given cache (or memory) size (Number of page frames that cache can hold at a time).
# The LRU caching scheme is to remove the least recently used frame when the cache is full and a new page is referenced which is not there in cache.
# Please see the Galvin book for more details (see the LRU page replacement slide here).
#
# https://www.geeksforgeeks.org/lru-cache-implementation/


from collections import defaultdict


class LRU:

    def __init__(self, n):
        self.cache = []
        self.n = n
        self.dic = defaultdict()  # page number as key, queue location as value

    def enqueue(self, data):
        if len(self.cache) == self.n:
            self.dequeue()

        self.cache.append(data)
        self.dic[data] = len(self.cache)-1

    def dequeue(self):
        self.cache.pop(0)







