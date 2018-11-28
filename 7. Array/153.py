class Solution(object):
    def findMin(self, nums):

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]


        l = 0
        r = len(nums)
        if nums[r-1] > nums[l]:
            return nums[l]
        else:
            while True:
                i = (l+r)//2
                if nums[i] < nums[i-1]:
                    return nums[i]
                if nums[i] > nums[l]:
                    l = i
                else:
                    r = i
s = Solution()
print(s.findMin([1,2]))