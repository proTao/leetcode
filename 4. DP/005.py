class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def manachers(S):
            A = '!#' + '#'.join(S) + '#?'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            # print(list(A))
            # print(list(map(str,Z)))
            return A,Z
        changed_s, dp = manachers(s)
        mr = 0
        ms = 0
        for i,r in enumerate(dp):
            if r > mr:
                mr = r
                ms = changed_s[i-r:i+r+1]
        return ms.replace("#","")

print(Solution().longestPalindrome("b"))