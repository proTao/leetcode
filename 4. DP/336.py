class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        if n <= 3:
            return n-1
        for i in range(2, n+1):
            # 
            # print(i)
            for j in range(2, i//2+1):
                # print("\t", dp[j], dp[i-j])
                if dp[j] * dp[i-j] > dp[i]:
                    dp[i] = dp[j] * dp[i-j]

        # print(dp)
        return dp[-1]
s=Solution()
print(s.integerBreak(10))