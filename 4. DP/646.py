class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        # O(nlgn)
        pairs = sorted(pairs, key=lambda x: (x[1], -x[0]))
        print(pairs)
        earlyest_end = pairs[0][1]
        # (end_point , max mission count)
        dp = [(pairs[0][1], 1)]

        for start, end in pairs[1:]:
            if end != dp[-1][0]:
                last_end, opt = dp[-1]

                # 怎样快速的在bp中找到小于k的子问题的解
                if last_end >= start:
                    for last_end, subq in dp[-2::-1]:
                        # 往前搜索子问题的解
                        print("back",last_end,subq)
                        if last_end < start:
                            if subq + 1 > opt:
                                opt = subq + 1
                            break
                else:
                    opt += 1
                print(end, opt, dp)
                dp.append((end, opt))
                

        print(dp)
        return dp[-1][1]

class Solution1:
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
                print(start, end, dp)
                for e, (x, _) in dp.items():
                    if e < start and x > opt:
                        opt = x
                dp[end] = (opt+1, start)
                if opt + 1 > res:
                    res = opt + 1

        # print(dp)
        return res



pairs = [[1,2],[3,4],[5,6],[7,10],[11,12],[1,8],[9,13]]
s = Solution1()
print(s.findLongestChain(pairs))