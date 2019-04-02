from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for i, count1 in c1.items():
            if i in c2:
                res.extend([i] * min(count1, c2[i]))
        
        return res