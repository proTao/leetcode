class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float("-inf")] + nums + [float("-inf")]
        lower = 1
        upper = len(nums) - 1
        while lower < upper:
            # print(lower, upper)
            mid = (upper + lower) >> 1
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid-1
            elif nums[mid] > nums[mid+1]:
                upper = mid
            else:
                lower = mid + 1
        return mid-1

l = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(l))