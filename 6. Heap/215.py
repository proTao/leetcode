from numpy import argmax
from random import randrange
import bottleneck

class Solution(object):
    def findKthLargest(self, nums, k):
        return self.helper(nums, k, len(nums))

    def helper(self, nums, k, l=0):
        threshold = 3
        # by sorted, can AC 
        if l <= threshold:
            a=sorted(nums)
            return a[l-k]
        else:
        # quite select by partition

        # select a pivot
            index = [randrange(0, l-1) for i in range(3)]
            pivot = index[argmax(nums[i] for i in index)]

            # make the pivot at the first position
            nums[0], nums[pivot] = nums[pivot], nums[0]

            # patition : bigger in the left and smaller in the right
            i = 1
            j = l-1
            while True:
                while(nums[j] < nums[0] and j > 0):
                    j -= 1
                while(nums[i] > nums[0] and i < l-1):
                    i += 1
                if i >= j:
                    break
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            nums[0],nums[j] = nums[j],nums[0]


            # recursion
            if j+1 == k:
                return nums[j]
            if j+1 > k:
                return self.helper(nums[:j], k, j)
            if j+1 < k:
                return self.helper(nums[j+1:],k-j-1, l-j-1)
        

import heapq

class Solution1:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            # if n > heap[0]:
            heapq.heappushpop(heap, n)
        return heap[0]    

nums = [i for i in range(2000000)]
k = 150
from random import shuffle
import cProfile, pstats
shuffle(nums)
cProfile.run("Solution().findKthLargest(nums, k)","timeit")
p = pstats.Stats('timeit')
p.sort_stats('time')
p.print_stats()

