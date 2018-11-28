from itertools import accumulate
from pprint import pprint

class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        dp = [[None] * len(nums) for _ in range(m)]
        dp[0] = list(accumulate(nums))
        for i in range(m):
            dp[i][0] = nums[0]
        for i in range(1,m):
            for j in range(1, i+1):
                dp[i][j] = max(dp[i][j-1], nums[j])

        sum_dict = {}
        for i in range(len(nums)):
            temp_sum = 0
            for j in range(i, len(nums)):
                temp_sum += nums[j]
                sum_dict[(i,j)] = temp_sum
        # pprint(sum_dict)
        # pprint(dp)

        for i in range(1, m):
            for j in range(i+1, len(nums)):
                k = j
                temp_res = float("inf")
                while k >= i:
                    split = max(sum_dict[(k,j)], dp[i-1][k-1])
                    if split < temp_res:
                        temp_res = split
                    if sum_dict[(k,j)] > dp[i-1][k-1]:
                        break
                    k -= 1
                dp[i][j] = temp_res
        # pprint(dp)
        return dp[-1][-1]

    
print(Solution().splitArray([1,2,4,5,3], 3)) # 5
# print(Solution().splitArray([7,2,5,10,8], 2)) # 18
# print(Solution().splitArray([2,3,1,2,4,3], 5)) # 4