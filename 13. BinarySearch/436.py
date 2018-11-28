from bisect import bisect_left
from operator import itemgetter
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        length = len(intervals)
        start = [None] * length
        # end = [None] * length
        res = [None] * length

        for i in range(length):
            start[i] = (intervals[i].start, i)
            # end[i] = intervals[i].end
        start.sort(key = itemgetter(0))
        print(start)
        for i in range(length):
            res_index = bisect_left(start, (intervals[i].end, float("-inf")))
            if res_index < length:
                res[i] = start[res_index][1]
            else:
                res[i] = -1
        return res

intervals = [Interval(3,4),Interval(2,3), Interval(1,2)]
print(Solution().findRightInterval(intervals))
