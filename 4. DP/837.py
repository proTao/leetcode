from itertools import accumulate
class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        gap = N - K
        dp = [1] + [1] * gap
        acc = [0] + list(accumulate(dp))

        for n in range(gap+1, N+1):
            dp.append((acc[-1] - acc[-min(W, n)-1]) / W)
            acc.append(acc[-1]+dp[-1])
        print(dp)
        return dp[-1]

print(Solution().new21Game(21, 17, 10))