coding = {
'1','2','3','4','5','6','7','8','9','10',
'11','12','13','14','15','16','17','18','19','20',
'21','22','23','24','25','26'
}


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [1] * (len(s)+1)
        if s[0] == '0':
            dp[1] = 0

        for i, c in enumerate(s[1:],2):
            dp[i] = dp[i-1] if c != '0' else 0
            if s[i-2:i] in coding:
                dp[i] += dp[i-2]
        print(dp)
        return dp[-1]

print(Solution().numDecodings('12'))
        