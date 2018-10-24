class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        maxPro = 0
        # 子问题：   （前k个元素最小值， 第k个元素）
        subQues = (prices[0], prices[0])
        for x in prices[1:]:
            subQues = min(x, subQues[0]), x
            maxPro = max(maxPro, subQues[1]-subQues[0])
            print(subQues)

        return maxPro

s = Solution()
print(s.maxProfit([7,1,5,0,6,4]))