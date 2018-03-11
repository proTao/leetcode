class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        current = 0

        for e in nums:
            if count == 0:
                current = e
                count = 1
            else:
                if e == current:
                    count += 1
                else:
                    count -= 1

        return current