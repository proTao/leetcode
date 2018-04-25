class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        # O(nlgn)
        pairs = sorted(pairs, key=lambda x: (x[1], -x[0]))
        print(pairs)

        # end_point : max mission count, start
        dp = {}
        res = 0

        for start, end in pairs:
            opt = 0
            if end not in dp:
                for e, (x, _) in dp.items():
                    if e < start and x > opt:
                        opt = x
                dp[end] = (opt+1, start)
                if opt + 1 > res:
                    res = opt + 1

        # print(dp)
        return res



pairs = [[1,2], [2,3], [3,4]]
s = Solution()
print(s.findLongestChain(pairs))