from itertools import accumulate

class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0 and 0 not in nums:
            return False

        if 0 in nums:
            i = nums.index(0)
            while True:
                try:
                    j = nums.index(0, i+1)
                    if j - i == 1:
                        return True
                    i = j
                except ValueError as e:
                    break

            if k == 0:
                return False

            

        # k > 0
        mod = [i % k for i in accumulate(nums)]
        if 0 in mod[1:]:
            return True
        index = {}
        for i, m in enumerate(mod):
            if m not in index:
                index[m] = i
            else:
                if i - index[m] > 1:
                    return True
        return False

a = [1,1]
k = 2

# a=[0, 1, 0, 0]
# k = 0
print(Solution().checkSubarraySum(a,k))
