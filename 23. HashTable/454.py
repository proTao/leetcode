from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        c = Counter(i+j for i in C for j in D)
        res = 0
        for i in A:
            for j in B:
               res += c[-i-j] 
        return res

if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    print(Solution().fourSumCount(A, B, C, D))