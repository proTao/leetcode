from random import random
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        CDF = [0]
        total_weight = sum(w)
        for i in w:
            CDF.append(CDF[-1] + i)
        self.CDF = list(map(lambda x:x/total_weight, CDF))
        print(self.CDF)

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random()
        lower, upper = 0, len(self.CDF)
        while lower < upper:
            mid = (lower + upper) >> 1
            if self.CDF[mid] == target:
                return mid - 1
            elif self.CDF[mid] < target:
                lower = mid + 1
            else:
                if upper == mid + 1:
                    break
                else:
                    upper = mid + 1
        for i in range(lower, upper):
            if self.CDF[i] > target:
                return i - 1



# Your Solution object will be instantiated and called as such:
obj = Solution([1,3,5,1])
samples = [obj.pickIndex() for _ in range(5000)]
from collections import Counter
print(Counter(samples))