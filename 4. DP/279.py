dp = [None,1]
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if len(dp) > n:
            return dp[n]
        for j in range(len(dp),n+1):
            sqrt = int(j**0.5)
            if sqrt ** 2 == j:
                dp.append(1)
            else:
                dp.append(min(dp[j-i**2] for i in range(1, sqrt+1)) + 1)

        return dp[-1]

if __name__ == "__main__":
    print(Solution().numSquares(12))
    print(dp)
    print(Solution().numSquares(13))
    print(dp)