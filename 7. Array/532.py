class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # because k is absolute diff
        if k < 0:
            return 0

        pairs = set()
        sorted_nums = sorted(nums)
        if k == 0:
            for i in sorted_nums:
                if sorted_nums.count(i) > 1:
                    pairs.add((i,i))
            count = len(pairs)
        else:
            sorted_nums_add_k = map(lambda x:x+k, sorted_nums)
            count = len(set(sorted_nums).intersection(set(sorted_nums_add_k)))

        # print(pairs)
        return count

s = Solution()
print(s.findPairs([3,1,4,1,5],2))
print(s.findPairs([1,2,3,4,5],1))
print(s.findPairs([1,3,1,5,4],0))

print(s.findPairs([1,2,3,4,5],-1))
