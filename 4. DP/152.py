class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bound
        if len(nums) == 1:
            return nums[0]

        # initial
        max_prod = nums[0] if nums[0] > 0 else 0
        minus_max_prod = nums[0] if nums[0] < 0 else 0
        res = max_prod

        # dp
        for i,n in enumerate(nums[1:], start=1):
            if n > 0:
                max_prod, minus_max_prod = max(max_prod * n, n), minus_max_prod * n
            elif n == 0:
                max_prod = minus_max_prod = 0
            else:
                max_prod, minus_max_prod = minus_max_prod * n, min(max_prod * n, n)
            if max_prod > res:
                res = max_prod
            print(max_prod)
            print(minus_max_prod)
            print()

        return res

a=[-4,-3,-2]

print("result :", Solution().maxProduct(a))