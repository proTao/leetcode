# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version < 10:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n + 1
        while lower < upper:
            mid = (lower + upper) // 2
            if isBadVersion(mid):
                if upper == mid + 1:
                    break
                else:
                    upper = mid + 1
            else:
                lower = mid + 1
        
        for i in range(lower, upper):
            if isBadVersion(i):
                return i

print(Solution().firstBadVersion(20))
                