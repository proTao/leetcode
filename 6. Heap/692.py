from collections import Counter
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, s, k):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        print(c)
        heap = [(-count,char) for (char,count) in c.items()]

        heapify(heap)

        res = [0] * k
        for i in range(k):
            count, char = heappop(heap)
            res[i] = char
        return res

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topKFrequent(words, k))