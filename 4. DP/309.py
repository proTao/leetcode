class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        you can not immediatelly buy afer sell
        """
        if len(prices) <= 1:
            return 0
        state1_cash = 0
        state1_hold = -prices[0]
        state2_cash = max(prices[1]-prices[0], 0)
        state2_hold = max(-prices[0], -prices[1])
        print(state1_cash, state1_hold)

        for p in prices[2:]:
            temp = state1_cash
            state1_cash, state1_hold = state2_cash, state2_hold
            state2_cash = max(state2_cash, state2_hold+p)
            state2_hold = max(state2_hold, temp-p)
            print(state2_cash, state2_hold)

p = [3,2,4,7,5,1]
print(Solution().maxProfit(p))