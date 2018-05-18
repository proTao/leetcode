class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1] * min(m,n)
        r = max(m,n)
        for _ in range(r-1):
            for i in range(1,len(l)):
                l[i] = l[i] + l[i-1]
            print(l)
        return l[-1]
        
print(Solution().uniquePaths(4,5))