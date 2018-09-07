class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        length = len(nums)
        min_delta = float("inf")
        res = None

        nums.sort()
        for i, val in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            for left, left_val in enumerate(nums[i+1:-1],start=i+1):
                while left < right and left_val + nums[right] + val > target:
                    right -= 1
                if left < right and left_val + nums[right] + val == target:
                    return target
                elif left < right and \
                    (   right == length-1 or\
                            abs(left_val + nums[right] + val - target) <\
                            abs(left_val + nums[right+1] + val - target)\
                    ):
                    if abs(left_val + nums[right] + val - target) < min_delta:
                        res = left_val + nums[right] + val
                        min_delta = abs(left_val + nums[right] + val - target)
                else: # maybe left == right
                    if abs(left_val + nums[right+1] + val - target) < min_delta:
                        res = left_val + nums[right+1] + val
                        min_delta = abs(left_val + nums[right+1] + val - target)
        return res

a = [-5,1,2,3,4,7]
t = 1
a = [-1,2,1,-4]
t = 1
print(Solution().threeSumClosest(a, t))

