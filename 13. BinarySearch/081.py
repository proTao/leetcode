from bisect import bisect_left
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        # if len(nums) == 1:
        #     return nums[0] == target
        lower = 0
        upper = len(nums)-1
        while lower <= upper:
            if nums[lower] < nums[upper]:
                index = bisect_left(nums[lower:upper+1], target)
                return index < upper+ 1-lower and nums[lower:upper+1][index] == target
            else:
                mid = (lower + upper) >> 1
                mid_val = nums[mid]
                if mid_val == target:
                    return True
                if mid_val >= nums[lower]:
                    if nums[lower] <= target < mid_val:
                        upper = mid - 1
                    else:
                        lower = mid + 1
                else:
                    if mid_val < target <= nums[upper]:
                        lower = mid + 1
                    else:
                        upper = mid - 1
        return False

nums = [4,5,6,7,0,1,2]
target = 3
nums = [1,3]
target = 4
nums = [3,1]
target = 1
print(Solution().search(nums, target))