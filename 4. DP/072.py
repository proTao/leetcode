from pprint import pprint
from copy import copy
D_I_SCORE = 0   # Delete / Insert
R_SCORE = 0     # Replace
S_SCORE = 1     # Same


class Solution:
    # solve the max score
    def minDistanceNaive(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [0] * (len(word1) + 1)
        dp_new  = [0] * (len(word1) + 1)

        for i in range(1, len(word1)+1):
            dp[i] = D_I_SCORE * i


        # print(dp)
        for i in range(1, len(word2)+1):
            dp_new[0] = D_I_SCORE * i
            for j in range(1, len(word1)+1):
                dp_new[j] = max(
                    dp[j-1] + R_SCORE, 
                    max(dp_new[j-1], dp[j]) + D_I_SCORE
                    ) if word2[i-1] != word1[j-1] else dp[j-1] + S_SCORE
            # print(word2[i-1])
            # pprint(dp_new)
            dp = copy(dp_new)
        return dp

    def minDistance(self, word1, word2):
        forward = self.minDistanceNaive(word2, word1[:len(word1)//2])
        backward = self.minDistanceNaive(word2[::-1], word1[len(word1)//2:][::-1])[::-1]
        p, score = max(((i,f+b) for i, (f, b) in enumerate(zip(forward, backward))), key=lambda x:x[1])
        print(p, score)
        print(word1[:len(word1)//2], word2[:p])
        print(word1[len(word1)//2:], word2[p:])
        # p_l, _ = self.minDistance(word1[:len(word1)//2], word2[:p+1])
        # p_r, _ = self.minDistance(word1[len(word1)//2:], word2[p+1:])

        # return p_l + p + p_r

s = Solution()
w1="ocurrance"
w2="occurrence"
print(s.minDistance("","bb"))