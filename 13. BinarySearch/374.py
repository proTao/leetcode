# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
target = 6
def guess(x):
    if x == target:
        return 0
    elif x < target:
        return -1
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i < j:
            mid = (i+j) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                j = mid
            else:
                i = mid+1
        return i


print(Solution().guessNumber(10))