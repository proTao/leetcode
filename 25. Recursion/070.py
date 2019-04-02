from functools import lru_cache
class Solution:
    @lru_cache(100, True)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)