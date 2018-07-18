class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums) // 2
        if target * 2 != sum(nums):
            return False

        dp = [True] + [False] * target
        print(dp)


        for n in nums[::-1]:
            for i in range(target, n-1, -1):
                dp[i] = dp[i] or dp[i-n]
            # print(dp)
        return dp[-1]

print(Solution().canPartition([1,2,3,5]))
                

