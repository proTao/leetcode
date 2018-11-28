from math import ceil
from bisect import bisect_left

class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        # 找到小于等于H的最大
        a = A(piles)
        return bisect_left(a, -H)

    
class A:
    def __init__(self, piles):
        self.piles = piles
        self.length = max(piles)
    def __getitem__(self, speed):
        # 这是一个单调减的函数
        if speed == 0:
            return float("-inf")
        else:
            return -sum(ceil(i / speed) for i in self.piles)
    
    def __len__(self):
        return self.length

piles = [3,6,7,11]
H = 8 # res = 4

piles = [30,11,23,4,20]
H = 5 # res = 30

piles = [30,11,23,4,20]
H = 6 # res = 23

# print(Solution().minEatingSpeed(piles, H))
a = A(piles)
print(a[0])