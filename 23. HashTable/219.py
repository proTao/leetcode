from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {} # chr -> last index
        for i, x in enumerate(nums):
            if x in index_map:
                last_index = index_map[x]
                if i - last_index <= k:
                    return True
                index_map[x] = i
            else:
                index_map[x] = i
        return False

if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], k = 2))

