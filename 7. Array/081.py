class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # preprocess simple situation
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False

        cliff = self.findmax(nums)
        print("max position:",cliff)

        if target>=nums[0] and target<=nums[cliff]:
            res = self.binarySearch(nums, 0, cliff+1, target)
        else:
            if cliff != len(nums)-1:
                res = self.binarySearch(nums, cliff+1, len(nums), target)
            else:
                return False
        return True


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
                return False
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i
            else:
                l = i

s = Solution()
nums=[2,3,4,4,1,1]
target = 4
res = s.search(nums, target)
print(res)
