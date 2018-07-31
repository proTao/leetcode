from collections import Counter
from heapq import heapify, heappop


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        heap = [(-count,char) for (char,count) in c.items()]
        heapify(heap)

        res = [0] * len(s)
        i = 0
        while heap:
            count, char = heappop(heap)
            for _ in range(-count):
                res[i] = char
                i += 1

        return "".join(res)

print(Solution().frequencySort("raaeaedere"))