class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        lower = 0
        upper = abs(dividend)+1
        if dividend == 0:
            return 0
        else:
            negaive = (dividend > 0) ^ (divisor > 0)
            dividend = abs(dividend)
            divisor = abs(divisor)

        while lower < upper:
            mid = (lower+upper) >> 1
            if mid * divisor <= dividend:
                if lower != mid:
                    lower = mid
                else:
                    break
            else:
                upper = mid
        for i in range(lower, upper):
            if i * divisor > dividend:
                res = 1-i if negaive else i-1
                if res > 2 ** 31 -1:
                    return 2 ** 31 -1
                else:
                    return res
        res = 1-upper if negaive else upper-1
        if res > 2 ** 31 -1:
            return 2 ** 31 -1
        else:
            return res
        

print(Solution().divide(-2147483648, -1))