from pprint import pprint as print
import copy
direction = ((1,0),(-1,0),(0,1),(0,-1))
class Solution:
    def findPaths(self, m, n, N, x, y):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        x += 1
        y += 1
        if N == 0:
            return 0
        dp = [[0 for i in range(n+2)] for j in range(m+2)]
        for i in range(1,n+1):
            dp[0][i] = 1
            dp[1][i] = 1
            dp[-2][i] += 1
            dp[-1][i] += 1
        for i in range(1,m+1):
            dp[i][0] = 1
            dp[i][1] += 1
            dp[i][-2] += 1
            dp[i][-1] = 1


        # print(dp)
        dp2 = copy.deepcopy(dp)

        for r in range(N-2,-1,-1):
            if r % 2 == 0:
                update_dp(dp, dp2, x, y, r)
                # print(dp2)
            else:
                update_dp(dp2, dp, x, y, r)
                # print(dp)
            

        
        return max(dp[x][y],dp2[x][y]) % 1000000007

def update_dp(olddp, newdp, center_x, center_y, r):
    m = len(olddp)-2
    n = len(olddp[0])-2
    x_low = center_x - r
    x_high = center_x + r
    y_low = center_y - r
    y_high = center_y + r

    for i in range(max(1, x_low),min(m, x_high)+1):
        for j in range(max(1, y_low),min(n, y_high)+1):
            # print((i,j))
            newdp[i][j] = sum(olddp[x][y] for x,y in 
                map(lambda d: (i+d[0],j+d[1]), direction))

        # print("")




s = Solution()
print(s.findPaths(50,50,50,5,7))