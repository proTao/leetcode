class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        length = len(nums)
        sub_sum = 0
        fast = 0
        res = length
        for slow, val in enumerate(nums):
            while fast < length and sub_sum < s:
                sub_sum += nums[fast]
                fast += 1
                
            if fast == length and sub_sum < s:
                break
            res = min(res, fast - slow)
            sub_sum -= val
        return res

a = [2,3]
print(Solution().minSubArrayLen(7,a))
