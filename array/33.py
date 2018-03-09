class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # preprocess simple situation
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        cliff = self.findmax(nums)
        # print(cliff)

        if target>=nums[0] and target<=nums[cliff]:
            return self.binarySearch(nums, 0, cliff+1, target)
        else:
            if cliff != len(nums)-1:
                return self.binarySearch(nums, cliff+1, len(nums), target)
            else:
                return -1



    def findmax(self, nums):
        """
        if input 34512
        return 2(the position of 5)
        """
        l = 0
        r = len(nums)-1
        if nums[r] > nums[l]:
            return r
        else:
            while True:
                i = (l+r)//2
                if nums[i] > nums[i+1]:
                    return i
                if nums[i] > nums[l]:
                    l = i
                else:
                    r = i

    def binarySearch(self, nums, l, r, target):
        # search range = [l, r) or say [l, r-1]
        while(True):
            i = (l+r)//2
            if i == l and nums[i] != target:
                return -1
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i
            else:
                l = i

s = Solution()
nums=[2,3,4,1]
target = 1
res = s.search(nums, target)
print(res)
