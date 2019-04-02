class Solution:
    def removeElement1(self, nums, target):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        fast = 0
        length = len(nums)
        while fast < length:
            while slow < length and nums[slow] != target:
                slow += 1
            fast = max(fast, slow)
            while fast < length and nums[fast] == target:
                fast += 1
            if fast < length:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1

        return slow
    
    def removeElement(self, nums, val):
        # 上面的方法更清晰的版本
        i = 0;
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    
    def removeElement2(self, nums, val):
        """
        稍微好一点点的解法
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1];
                n -= 1
            else :
                i += 1
        return n


if __name__ == "__main__":
    a = [2,2,3,3]
    print(Solution().removeElement(a, 3))
