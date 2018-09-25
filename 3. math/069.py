from math import floor
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        threshold = 1e-6
        r = x
        while r*r > x:
            new_r = (r + x/r) / 2
            if abs(new_r-r) < threshold:
                break
            r = new_r
        return floor(r)

print(Solution().mySqrt(122))