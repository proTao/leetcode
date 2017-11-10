class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # approach 1: append
        nonezero=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonezero] = nums[i]
                nonezero += 1

        while nonezero < len(nums):
            nums[nonezero]=0
            nonezero+=1

        return nums

        # approach 2: when you meet a nonezero, swap, so you don't need modify the rest part to zero at last

s=Solution()
a=[1,0,2,4,0,0,0,2,4,9,0]
print(s.moveZeroes(a))
print(a)