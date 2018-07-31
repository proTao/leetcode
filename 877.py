class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        length = len(piles)
        if length == 1:
            return True

        dp = {(i,i):n for i,n in enumerate(piles)}
        print(dp)

        for l in range(1,length):
            for i in range(0, length-l):
                dp[(i,i+l)] = max(piles[i]-dp[(i+1,i+l)], piles[i+l]-dp[(i,i+l-1)])
        return dp[(0,length-1)] > 0
        
print(Solution().stoneGame([5,3,4,5]))
