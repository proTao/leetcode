class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]
        for i in range(2, n+1):
            res = sum(dp[j1] * dp[j2] * 2 for j1, j2 in self.getSplit(i))
            if i % 2 == 1:
                res += dp[i//2] ** 2
            dp.append(res)
            print(dp)
        return dp[-1]

    def getSplit(self, n):
        for i in range(n):
            if i < n//2:
                yield (i, n-i-1)
            i += 1

print(Solution().numTrees(3))
        