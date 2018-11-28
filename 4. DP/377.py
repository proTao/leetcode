class Solution:
    def combinationSum4(self, nums, target):
        # 
        nums = sorted(nums)
        dp = [1] + [0] * target
        print(dp)

        for t in range(1, target+1):
            res = 0
            for n in nums:
                if n > t:
                    break
                res += dp[t-n]
            dp[t] = res
            print(res)
        return dp[-1]


print(Solution().combinationSum4([1,2,3,4], 4))    