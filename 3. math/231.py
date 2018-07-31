import math

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 2**int(math.log2(n)) == n
print(Solution().isPowerOfTwo(2))