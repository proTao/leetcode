class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        if n == 2:
            return 2

        f_2 = 1
        f_1 = 2
        i = 3

        while i < n:
            f_1, f_2 = f_1 + f_2, f_1 
            i += 1
        return f_1 + f_2

print(Solution().climbStairs(4))
