class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        if target > nums[-1] or target < nums[0]:
            return -1
        while i<=j:
            mid = (i + j) >> 1
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid + 1
                if nums[i] > target:
                    return -1
            else:
                j = mid - 1
                if nums[j] < target:
                    return -1

nums = [-1,0,3,5,9,12]
target = 13
print(Solution().search(nums, target))