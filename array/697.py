class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        # print(d)
        max_v = [0]
        max_k = -1
        for k,v in d.items():
            if v > max_v:
                max_v = [v]
                max_k = k
            if v = max_v[0]:
        if max_v == 1:
            return 1

        i = nums.index(max_k)
        j = len(nums) - nums[::-1].index(max_k)
        return j-i

s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1]))


