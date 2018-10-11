class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [1, 2, 4]
        for i in range(3, N+1):
            # print(dp)
            dp.append((2*dp[-1] + dp[-3]) % 1000000007)
        # print(dp)
        return (dp[N] - dp[N-1] + 1000000007) % 1000000007

print(Solution().numTilings(30))
