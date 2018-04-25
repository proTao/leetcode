from pprint import pprint as print

class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        # A = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        # become elegant
        A = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

        for i in range(len(s1)):
            A[0][i+1]=ord(s1[i])+A[0][i]
        for i in range(len(s2)):
            A[i+1][0]=ord(s2[i])+A[i][0]

        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                A[i][j] = min(A[i][j-1] + ord(s1[j-1]), A[i-1][j] + ord(s2[i-1])) \
                               if s2[i-1] != s1[j-1] \
                               else A[i-1][j-1]

        return A[-1][-1]

class SolutionPythonic:
    # 大牛写的Pythonic的代码
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for (i1, c1), (i2, c2) in itertools.product(enumerate(s1), enumerate(s2)):
            dp[i1 + 1][i2 + 1] = dp[i1][i2] + ord(c1) if c1 == c2 else max(dp[i1][i2 + 1], dp[i1 + 1][i2])
        return sum(map(ord, s1 + s2)) - dp[-1][-1] * 2

s = Solution()
print(s.minimumDeleteSum("sea", "eat"))