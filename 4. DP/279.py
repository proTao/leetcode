class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        dp = [0] * (n+1)
        dp[1] = 1

        for j in range(2,n+1):
            sqrt = int(j**0.5)
            if sqrt ** 2 == j:
                dp[j] =  1
            else:
                dp[j] = min(dp[j-i**2] for i in range(1, sqrt+1)) + 1

        return dp[-1]