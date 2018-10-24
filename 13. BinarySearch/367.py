class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        lower = 1
        upper = num
        while lower <= upper:
            mid = (lower + upper) >> 1
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                upper = mid - 1
            else:
                lower = mid + 1
        return False

print(Solution().isPerfectSquare(1))
