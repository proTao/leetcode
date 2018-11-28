class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[1]*nums[-1] >= 0:
            return nums[-1]*nums[-2]*nums[-3]
        else:
            return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])