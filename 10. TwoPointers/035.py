class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 :
            return []
        nums = sorted(nums)
        i = 0
        last_i = last_j = last_k = None
        res = []
        while i < len(nums)-2:
            if last_i == nums[i]:
                i += 1
                continue
            last_i = nums[i]
            j = i + 1
            last_j = None
            k = len(nums)-1
            while j < k:
                if nums[j] == last_j:
                    j += 1
                    continue
                last_j = nums[j]
                while nums[i] + nums[j] + nums[k] > 0 and j < k:
                    k -= 1
                if j < k and nums[i] + nums[j] + nums[k] == 0:
                    res.append([last_i, last_j, nums[k]])

                j += 1
            i += 1
        return res

nums = [1,2,-2,-1]
print(Solution().threeSum(nums))    