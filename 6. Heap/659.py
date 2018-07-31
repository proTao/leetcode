import heapq
from collections import defaultdict
class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False

        length_ends_with = defaultdict(list)
        for n in nums:
            if not length_ends_with[n-1]:
                heapq.heappush(length_ends_with[n], 1)
            else:
                shortest_ends_with_n = heapq.heappop(length_ends_with[n-1])+1
                heapq.heappush(length_ends_with[n], shortest_ends_with_n)
                
        for i in filter(lambda x:x, length_ends_with.values()):
            if min(i) < 3:
                return False
        return True

    
    def isPossible1(self, nums):
        import collections
        left = collections.Counter(nums)
        end = collections.Counter()

        print(left, end)
        for i in nums:
            if not left[i]:
                continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        print(left, end)
        return True
                

print(Solution().isPossible1([1,1,2,2,3]))     
