class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        current_max = 1
        for i, n in enumerate(nums):
            try:
                # print(list(dp[j] for j,_ in filter(lambda x:x[1] < n, enumerate(nums[:i]))))
                dp[i] = max(dp[j] for j,_ in filter(lambda x:x[1] < n, enumerate(nums[:i])))+1
            except Exception:
                dp[i] = 1

            print(dp)

        return max(dp)

print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))