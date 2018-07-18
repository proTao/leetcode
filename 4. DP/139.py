class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # bound
        if len(wordDict) == 0:
            return False

        # initial
        word_set = set(wordDict)
        dp = [True] + [False] * len(s)
        max_l = max(len(i) for i in word_set)
        for t2 in range(1,len(s)+1):
            # for t1 in range(max(0, t2 - max_l), t2):
            #     # print(s[t1:t2])
            #     if s[t1:t2] in word_set and dp[t1]:
            #         dp[t2] = True
            #         continue

            # pythonic : same sa above
            dp[t2] = any(s[t1:t2] in word_set and dp[t1] for t1 in range(max(0, t2 - max_l), t2))
            print(dp)
        return dp[-1]  




s = "applepenapple"
wordDict = ["apple", "pen", "app"]
print(Solution().wordBreak(s, wordDict))