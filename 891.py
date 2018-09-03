class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = {}
        res = 0
        for i in range(len(A)-1):
            tmp = min(A[i],A[i+1]), max(A[i],A[i+1])
            res += tmp[1] - tmp[0]
            dp[(i,i+1)] = tmp
        for l in range(2,len(A)):
            for i in range(len(A)-l):
                a = dp[(i,i+l-1)]
                tmp = min(a[0], A[i+l]), max(a[1],A[i+l])
                res += tmp[1] - tmp[0]
                dp[(i, i+l)] = tmp
        return res

A = [2,1,3]
print(Solution().sumSubseqWidths(A))
