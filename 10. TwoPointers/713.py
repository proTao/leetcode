class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left = 0
        right = 0
        prod = 1
        res = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            print(left, right)
            res += right - left + 1
        return res


a = [10,5,2,6]
a = [10,5,3,2,1,1]
print(Solution().numSubarrayProductLessThanK(a, 100))