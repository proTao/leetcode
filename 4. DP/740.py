from collections import Counter, OrderedDict

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = list(OrderedDict(Counter(nums)).items())
        print(l)
        # for i in nums:

        if len(l) == 0:
            return 0
        if len(l) == 1:
            return l[0][0] * l[0][1]
        

        dp = [0] * (len(l)+1)
        dp[0] = 0
        dp[1] = l[0][0] * l[0][1]
        print(1, dp)

        for i in range(2,len(l)+1):
            if l[i-2][0] == l[i-1][0]-1:
                dp[i] = max(dp[i-1], dp[i-2]+l[i-1][0]*l[i-1][1])
            else:
                dp[i] = dp[i-1] + l[i-1][0]*l[i-1][1]
            print(i,dp)
        return dp[-1]



print(Solution().deleteAndEarn([1, 3]))