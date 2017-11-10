class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # approach 1: swap
        # i=0
        # while i < len(nums):
        #     print(i)
        #     if nums[i]-1 != i and nums[i] != nums[nums[i]-1]:
        #         # swap
        #         temp = nums[i]
        #         nums[i] = nums[temp-1]
        #         nums[temp-1] = temp
        #         i -= 1
        #     i += 1

        #     print(nums)

        # res = []
        # for i in range(len(nums)):
        #     if nums[i]-1 != i:
        #         res.append(i+1)

        # return res


        # approach 2 : use positive and negative to storage bonus information
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -nums[index]
            # print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))