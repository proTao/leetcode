import copy
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # dp = copy.copy(grid[0])
        dp = grid[0]
        for i in range(1,n):
            dp[i] = dp[i] + dp[i-1]
        # print(dp)
        for i in range(1,m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1,n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
            # print(dp)
        return dp[-1]


g=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().minPathSum(g))