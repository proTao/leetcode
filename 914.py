from collections import Counter
from functools import reduce
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        c = Counter(deck)
        x = reduce(gcd, c.values())
        return x>=2

l = [1,1,1,2,2,2,3,3]
print(Solution().hasGroupsSizeX(l))
