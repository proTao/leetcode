import random
from pprint import pprint
from collections import namedtuple

subQ = namedtuple("subQ", ["min","max"])
class Solution:
    def maxProfitNSpace(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # (min, max) to this time
        dp = [(prices[0], prices[0])]
        profit = 0
        sales = []
        for i, p in enumerate(prices[1:]):
            if dp[-1][1] - p >= fee:
                profit += max(dp[-1][1] - dp[-1][0] - fee, 0)
                dp.append((p, p))
                sales.append(True)
            else:
                # continue wait
                dp.append((min(p, dp[-1][0]), max(dp[-1][1], p)))
                sales.append(False)
        sales.append(True)
        profit += (dp[-1][1] - dp[-1][0] - fee if dp[-1][1] - dp[-1][0] > fee else 0)
        pprint(list(zip(prices,dp,sales)))
        return profit

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # (min, max) to this time
        maxi = prices[0]
        mini = prices[0]
        profit = 0
        for i, p in enumerate(prices[1:]):
            if maxi - p >= fee:
                profit += max(maxi - mini - fee, 0)
                maxi = mini = p
            else:
                maxi = max(p, maxi)
                mini = min(p, mini)

        profit += (maxi - mini - fee if maxi - mini > fee else 0)
        return profit

class StandardSolution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash





s1 = Solution()
s2 = StandardSolution()
i = 1
while i < 10000 and False:
    prices = [random.randrange(1,100)  for i in range(20)]
    fee = random.randrange(1,50)

    # print(prices)
    if i%100 == 0:
        print(i)
    if s1.maxProfit(prices, fee) != s2.maxProfit(prices, fee):
        print(prices)
        print(fee)
        break
    i+=1

prices = [5,4,1]
fee = 2
print(s1.maxProfit(prices, fee))
# print(s2.maxProfit(prices, fee))