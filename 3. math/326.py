import math

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 3**int(math.log(n, 3)) == n

print(Solution().isPowerOfThree(3))