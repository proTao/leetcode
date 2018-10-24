from random import randint
from functools import partial

rand7 = partial(randint, a=1, b=7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            rand_cand = (rand7()-1) * 7 + rand7()
            # break
            if rand_cand <= 40:
                break
        # return rand_cand
        return (rand_cand // 4) % 10

from collections import Counter
s = Solution()
c = Counter([s.rand10() for i in range(100000)])

print(len(c))
print(c)