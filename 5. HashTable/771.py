class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_type = set(J)
        res = 0
        for i in S:
            if i in jewels_type:
                res += 1
        return res
    def pythonicSolution(self, J, S):
            return sum(map(S.count, J))               # this one after seeing https://discuss.leetcode.com/post/244105

J = "aA"
S = "aAAbbbb"
print(Solution().pythonicSolution(J, S))