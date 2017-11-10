class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        length = len(nums)
        sum = 0
        for i in range(0,length,2):
            sum += sorted_nums[i]
        return sum