from random import random, randint
from itertools import accumulate
from bisect import bisect_left

class Solution:

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        areas = []
        for i in rects:
            areas.append((i[3]-i[1]+1)*(i[2]-i[0]+1))
        self.prior_cdf = [i / sum(areas) for i in accumulate(areas)]
        self.rects = rects

    def pick(self):
        """
        :rtype: List[int]
        """
        rect = self.rects[bisect_left(self.prior_cdf, random())]
        return randint(rect[0], rect[2]), randint(rect[1], rect[3])


# Your Solution object will be instantiated and called as such:
rects = [[-2,-2,-1,-1],[1,0,3,0]]
obj = Solution(rects)
res = {True:0, False:0}
for i in range(5000):
    res[obj.pick()[1]!=0] += 1
print(res[False]/res[True]) #0.75