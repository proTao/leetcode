class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # bound
        if len(nums) == 0:
            return []

        # initial
        nums.sort()
        dp = [1] * len(nums)
        backtrack = [-1] * len(nums)

        # dp
        for i, n in enumerate(nums[1:],1):
            temp_l = 0
            temp_index = -1
            for j in range(i-1, -1, -1):
                if n % nums[j] == 0 and dp[j] > temp_l:
                    temp_l = dp[j]
                    temp_index = j
                dp[i] = temp_l + 1
                backtrack[i] = temp_index

        # backtrack
        max_l = max(dp)
        res = []
        j = dp.index(max_l)
        while j != -1:
            res.append(nums[j])
            j = backtrack[j]
        return res[::-1]


def run()
    a=[2,3,4,5,6,7,8,9,10,11,12,24]
    print(Solution().largestDivisibleSubset(a))
