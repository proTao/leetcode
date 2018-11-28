class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [-1] * length
        nums = nums + nums
        max_index = []
        for i, val in enumerate(nums):
            if not max_index or val <= nums[max_index[-1]]:
                max_index.append(i)
                continue
            else:
                while max_index and val > nums[max_index[-1]]:
                    j = max_index.pop()
                    if j < length:
                        res[j] = nums[i]
                max_index.append(i)
        return res


a = [1,2,3,4,3]
print(Solution().nextGreaterElements(a))