class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # bound
        r = len(matrix)
        if r <= 1:
            return int('1' in matrix[0]) if r ==1 else 0
        c = len(matrix[0])
        if c == 1:
            return int(['1'] in matrix) if c == 1 else 0

        # initial
        dp = [[0]*c for _ in range(r)]
        res = 0
        for i in range(r):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                res = 1
        for i in range(c):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i] == 1:
                res = 1
        # dp
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                if dp[i-1][j] == dp[i][j-1] and matrix[i-dp[i-1][j]][j-dp[i-1][j]] == '0':
                    dp[i][j] -= 1
                res = max(res, dp[i][j])
        print(dp)
        return res ** 2


a=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
a=[['0']]
a=[['1','1'],['1','1']]
a=[["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
print(Solution().maximalSquare(a))