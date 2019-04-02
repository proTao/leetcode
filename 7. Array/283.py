class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if fast > slow:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1

a = [1,0,2,0,3]
Solution().moveZeroes(a)
print(a)

                



        