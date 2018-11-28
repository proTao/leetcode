class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        f = lambda x: (x ** 2 + x) >> 1
        lower = 1
        upper = (n >> 1) + 1 # 令n/2作为上界
        while lower <= upper:
            # print(lower, upper)
            mid = (lower + upper) >> 1
            if f(mid) == n:
                return mid
            elif f(mid) < n:
                if lower != mid:
                    lower = mid
                else:
                    break
            else:
                upper = mid - 1
        for i in range(lower, upper + 1):
            if f(i) > n:
                return i - 1
        else:
            return upper

for i in range(20):
    print(i, Solution().arrangeCoins(i))
# print(Solution().arrangeCoins(3))