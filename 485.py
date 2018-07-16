class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        ones = 0
        for i in nums:
            if i == 1:
                ones += 1
            else:
                if max_ones < ones:
                    max_ones = ones
                    # print(max_ones)
                ones = 0
        if max_ones < ones:
            max_ones = ones
        return max_ones

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1,1,1]))