class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        DEBUG = True
        wait_decrease = False
        wait_increase = False
        total_profit = 0
        buy_in = -1

        for i in range(len(prices)):

            if  i<len(prices)-1 and \
                (i == 0 and prices[i] < prices[i+1] or \
                i > 0 and prices[i] < prices[i-1] and prices[i] < prices[i+1] or \
                i > 0 and prices[i] == prices[i-1] and prices[i] < prices[i+1] and wait_increase):
                # price[i] is an local minimal price, so buy in
                    buy_in = prices[i]
                    wait_increase = False
                    wait_decrease = False
                    if DEBUG:
                        print(i,"buy in :", buy_in)
                    continue


            elif i > 0 and buy_in >= 0 and \
                (i == len(prices)-1 and prices[i] > prices[i-1] or \
                i == len(prices)-1 and prices[i] == prices[i-1] and wait_decrease or \
                i < len(prices)-1 and prices[i] > prices[i-1] and prices[i] > prices[i+1] or \
                i < len(prices)-1 and prices[i] == prices[i-1] and prices[i] > prices[i+1] and wait_decrease):
                    # price[i] is an local maximal price, so sell out
                    total_profit += (prices[i] - buy_in)
                    wait_decrease = False
                    wait_increase = False
                    if DEBUG:
                        print(i,"sell out :", prices[i])
                    continue
                

            else:
                pass

            if i < len(prices)-1 and prices[i] == prices[i+1]:
                # not absolute local optimal price, we must wait
                if i==0:
                    wait_decrease = True 
                    wait_increase = True
                elif prices[i] > prices[i-1]:
                    wait_decrease = True
                elif prices[i] < prices[i-1]:
                    wait_increase = True
                else:
                    pass
                if DEBUG:
                    print(i, "wait_increase:",wait_increase,"wait_decrease:",wait_decrease)

            else:
                if DEBUG:
                    print(i,"nothing","wait_increase:",wait_increase,"wait_decrease:",wait_decrease)

            


        return total_profit

s = Solution()

res = s.maxProfit([2,2,5,5,5,7,7,6])
print("res",res)

