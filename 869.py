from itertools import permutations
from math import log2
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return True

        history = set()

        for newN in filter(lambda x:x not in history, permutations(str(N))):
            if newN[0] != '0' and newN[-1] in ('2','4','6','8'):
                # print(newN)
                # log = log2(int(newN))
                # if log == int(log):
                #     return True
                if bin(int("".join(newN))).count('1') == 1:
                    return True
            history.add(newN)


        return False

print(Solution().reorderedPowerOf2(9827391263))