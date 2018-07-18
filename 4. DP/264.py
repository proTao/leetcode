import heapq

class Solution(object):
    def nthUglyNumber1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [True] * 6
        if n <= 5:
            return n
        # print(dp, n)
        count = 5
        i = 6

        while count < n:
            dp.append(False)
            if i % 2 == 0:
                dp[i] = dp[i//2]
            if dp[i] == False and i % 3 == 0:
                dp[i] = dp[i//3]
            if dp[i] == False and i % 5 == 0:
                dp[i] = dp[i//5]
            if dp[i]:
                count += 1
            i += 1

        # print([i for (i,f) in enumerate(dp) if f and i>0])
        return len(dp)-1

    def nthUglyNumber(self, n):
        dp = [1,2,3,4,5,6,8,9,10,12,15]
        base = [[20,4,5],[25,5,5],[12,6,2]]
        heapq.heapify(base)
        last_index = 5

        def update():
            res = heapq.heappop(base)
            next_ugly = res[0]
            if res[2] == 5:
                pass
            if res[2] == 3:
                res[2] = 5
                res[0] = res[1]*res[2]
                heapq.heappush(base, res)
            if res[2] == 2:
                nonlocal last_index
                res[2] = 3
                res[0] = res[1]*res[2]
                heapq.heappush(base, res)
                if res[1] == dp[last_index]:
                    heapq.heappush(base, [dp[last_index+1]*2, dp[last_index+1], 2])
                    last_index += 1
            if next_ugly > dp[-1]:
                dp.append(next_ugly)
        while len(dp) < n:
            update()

        # print(dp)
        return dp[n-1]
        # print(base)
        # print(last_index)

from heapq import heappush, heappop     
class StandardSolution:
    ugly = []
    def nthUglyNumber(self, n):
        if not StandardSolution.ugly:
            self._nthUglyNumber(17000)
        return self.ugly[n-1]
    def _nthUglyNumber(self, n):
        q, counted = [1], {1}
        for i in range(n - 1):
            m = heappop(q)
            StandardSolution.ugly.append(m)
            for mm in [2*m, 3*m, 5*m]:
                if mm not in counted:
                    heappush(q, mm)
                    counted.add(mm)        
        return heappop(q)






a=StandardSolution()
print(a.nthUglyNumber(500))
