class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # first partition
        i = 0
        j = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            if i >= len(nums):
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        # print(nums, i, j)
        i = j
        while i < len(nums):
            while i < len(nums) and nums[i] != 1:
                i += 1
            if i >= len(nums):
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        # print(nums, i, j)

print(Solution().sortColors([2,0,2,1,1,0]))