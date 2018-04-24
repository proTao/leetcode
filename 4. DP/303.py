from pprint import pprint as print
class NumArray1:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.memo = {(i,i+1):nums[i] for i in range(len(nums))}

        for i in range(2, len(nums)+1):
            for j in range(len(nums)+1-i):
                self.memo[(j, j+i)] = self.memo[(j,j+i-1)]+\
                                        self.memo[(j+i-1,j+i)]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.memo[(i,j+1)]

from itertools import accumulate as acc
def NumArray(nums):
    cumsum = []
    cumsum = list(acc(nums))
    def sumRange(i, j):
        nonlocal cumsum
        return cumsum[j] - (cumsum[i-1] if i > 0 else 0)

    def caller():
        pass
    caller.sumRange = sumRange
    return caller

nums = [-2, 0, 3, -5]
s = NumArray(nums)
print(s.sumRange(1,3))

