class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        if(l == 0):
            return

        k = k % l
        self.rollback(nums, 0, l-k-1)
        self.rollback(nums, l-k, l-1)
        self.rollback(nums, 0,l-1)
    def rollback(self, nums, i, j):
        while(j>i):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

nums = [1,2]
s = Solution()
s.rotate(nums, 3)

print(nums)
