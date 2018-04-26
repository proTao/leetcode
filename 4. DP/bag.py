from pprint import pprint as print
from collections import namedtuple
from itertools import islice
from random import shuffle

class Solution:
    def bagging(self, items, bag_size):

        dp = [[0] * (bag_size+1) for i in range(len(items)+1)]
        print(dp)
        for i in range(1, len(items) + 1):
            print("")
            for j in range(1, bag_size + 1):
                dp[i][j] = max(dp[i-1][j], \
                            dp[i-1][j-items[i-1].weight] + items[i-1].value if j-items[i-1].weight >= 0 else 0 \
                            )
            print(dp)







Item = namedtuple("Item", ["value", "weight"])
s = Solution()
v = 7,1,3,2, 10
w = 12,2,7,5, 9
items = [Item(*i) for i in zip(v,w)]
shuffle(items)
bag_size = 15
s.bagging(items, bag_size)