class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        i = j = 1
        count = 1 # 当前i指向的元素前面有几个连续相同的数字
        while i < len(nums):
            last_val = nums[i-1]
            while count >= 2 and i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            if i == len(nums):
                break
            if nums[i] != nums[i-1]:
                count = 1

            nums[j] = nums[i]
            if nums[i] == last_val:
                count += 1
            i += 1
            j += 1
            # print(nums)
        return j

    
a = [0,0,1,1,1,1,2,3,3]
a = [1,1,1]
print(Solution().removeDuplicates(a))