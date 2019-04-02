from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in nums:
            if target - i in seen:
                return True
            else:
                seen.add(i)
        return False