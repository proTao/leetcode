class Solution:
    def removeElement(self, nums, target):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(nums)
        if len(nums) == 0:
            return 0

        new_array_index = 0
        next_change_index  = len(nums)-1
        while True:
            new_array_index = self.findNextTarget(nums, new_array_index, target)
            next_change_index = self.findNextChange(nums, next_change_index, target)
            if new_array_index < next_change_index:
                nums[next_change_index], nums[new_array_index] = nums[new_array_index], nums[next_change_index]
            
            print(nums, new_array_index, next_change_index, nums)
            if(next_change_index <= new_array_index):
                break
        return new_array_index


    def findNextTarget(self,nums,start,target):
        i = start
        while i < len(nums) and nums[i] != target:
            i += 1
        return i

    def findNextChange(self,nums,start,target):
        # zhao dao xia yi ge qian mian de yuan su shi target de wei zhi
        # if input is 123456734567, start is 2, target is 3
        # then return 6(the position of the first 7)
        j = start
        while j > -1 and nums[j] == target:
            j -= 1
        return j

    def same(self, nums, val):
        i = 0;
        n = len(nums);
        while (i < n):
            if (nums[i] == val):
                nums[i] = nums[n - 1];
                n -= 1
            else:
                i += 1
        return n;

s = Solution()
nums = [1,2,0,0,3,0,0,3,0]
target = 0
res = s.same(nums, target)
print("res", res)
print("nums", nums)

