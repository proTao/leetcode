class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0
        current_min = prices[0]
        current_max = prices[0]
        candidate_min = prices[0]
        for price in prices:
            print("current_max : "+str(current_max))
            print("current_min : "+str(current_min))
            print("candidate_min : "+str(candidate_min))
            print()
            print("price : "+str(price))
            print()
            if price > current_max:
                current_max = price
            if price < candidate_min:
                candidate_min = price
            if price - candidate_min > current_max - current_min:
                current_max = price
                current_min = candidate_min

        return current_max - current_min

s=Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
