class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])

        B = [[0] * m for _ in range(n)]
        print(B)
        for i in range(m):
            for j in range(n):
                B[j][i] = A[i][j]
        return B


print(Solution().transpose([[1,2,3],[4,5,6]]))