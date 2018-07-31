from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return list(map(lambda x:x[0], Counter(nums).most_common(k)))


print(Solution().topKFrequent([], 1))