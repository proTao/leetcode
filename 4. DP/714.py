from collections import namedtuple

subQ = namedtuple("subQ", ["least"])

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [subQ(prices[0])]
        buyin = prices[0]
        
        for i,p in enumerate(prices[1:]):
            if p > dp[-1].least:
                dp.append(subQ(dp[-1].least))
            else:
                dp.append(subQ(p))

        print(dp)

prices = [1, 3, 2, 8, 4, 9]
fee = 2

s = Solution()
s.maxProfit(prices, fee)