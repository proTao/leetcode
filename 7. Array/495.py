class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        overlap = 0
        for i in range(len(timeSeries)-1):
            is_overlap = (timeSeries[i+1] - timeSeries[i]) < duration
            overlap += is_overlap and (duration - timeSeries[i+1] + timeSeries[i]) or 0
            print("+="+str(overlap))
        return len(timeSeries) * duration - overlap

s = Solution()
# print(s.findPoisonedDuration([1,4], 2))
# print(s.findPoisonedDuration([1,2], 2))
print(s.findPoisonedDuration([1,2,3,4,5], 5))
