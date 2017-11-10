class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                res.append(abs(nums[i]))
            print(nums)

        return res

s=Solution()
print(s.findDuplicates([1,2,3,2]))