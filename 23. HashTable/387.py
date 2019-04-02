from collections import Counter
from math import inf

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        alpha = "qwertyuiopasdfghjklzxcvbnm"
        res = inf
        for c in alpha:
            i = s.find(c)
            if i == -1:
                continue
            j = s.find(c, i+1)
            if j == -1:
                res = min(res, i)
        return res if res is not inf else -1
            

if __name__ == "__main__":
    print(Solution().firstUniqCharBetter("loveleetcode"))
