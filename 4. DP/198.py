class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        f_1 = max(nums[1], nums[0])
        f_2 = nums[0]
        i = 2

        while i < len(nums):
            print(f_1, f_2)
            f_1, f_2, i = max(f_1, f_2 + nums[i]), f_1, i+1

        return f_1

print(Solution().rob([5,1,3,7,4,2]))