import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]  in ascending order 
        :type nums2: List[int]  in ascending order 
        :type k: int
        :rtype: List[List[int]]
        """

        
        l1 = len(nums1)
        l2 = len(nums2)
        res = []
        if l1 == 0 or l2 == 0:
            return res
        sums = [(nums1[0] + nums2[0], 0, 0)]
        used = set((0,0))

        while k > 0 and sums:
            _, i, j = heapq.heappop(sums)
            print(i,j)
            res.append([nums1[i], nums2[j]])
            if i + 1 < l1 and (i+1, j) not in used:
                used.add((i+1, j))
                heapq.heappush(sums, (nums1[i+1]+nums2[j], i+1, j))
            if j + 1 < l2 and (i, j+1) not in used:
                used.add((i, j+1))
                heapq.heappush(sums, (nums1[i]+nums2[j+1], i, j+1))
            k -= 1
        return res

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(Solution().kSmallestPairs(nums1, nums2, k))