class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane 算法
        if len(nums) < 1:
            return False
        max_memo = [nums[0]]

        for x in nums[1:]:
            max_memo.append(max(x, max_memo[-1]+x))

        print(max_memo)
        return max(max_memo)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))