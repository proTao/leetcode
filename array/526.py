class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        swappable_list = [[],]
        for i in range(1,N+1):
            swappable_list.append(self.findSwappable(i,N))

        for i,l in enumerate(swappable_list):
            print(i,l)
    
    def findReducible(self, x):
        if x == 1:
            return [1]
        res = []
        square_root_x = x**0.5//1
        i = 1
        while i <= square_root_x :
            if x%i == 0:
                res.append(i)
                res.append(x/i)
            i += 1
        return res

    def findTimerLessThanN(self, x, N):
        # not include x self
        i = N//x
        res = []
        while i > 1:
            res.append(x*i)
            i -= 1
        return res

    def findSwappable(self, x, N):
        res = self.findReducible(x)
        res.extend(self.findTimerLessThanN(x, N))
        return res

s = Solution()
res = s.countArrangement(5)
