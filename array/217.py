class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        appear = set()
        for i in nums:
            if i in appear:
                return True
            else:
                appear.add(i)
        else:
            return False

s=Solution()

print(s.containsDuplicate([1,2,3]))
