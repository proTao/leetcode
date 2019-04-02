from itertools import accumulate

'''
def accumulate(l):
    cur_sum = 0
    for i in l:
        cur_sum += i
        yield cur_sum
'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        leftsum = [0] + [i for i in accumulate(nums[:-1])]
        rightsum = [i for i in accumulate(nums[::-1][:-1])][::-1] + [0]
        for i in range(len(nums)):
            if leftsum[i] == rightsum[i]:
                return i
        return -1


if __name__ == "__main__":
    a = [0,0]
    print(Solution().pivotIndex(a))