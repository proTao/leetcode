from random import randrange
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        position = {}
        for i, n in enumerate(nums):
            if n in position:
                position[n].append(i)
            else:
                position[n] = [i]
        self.position = position

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        positions = self.position[target]
        count = 1
        res = 0
        for i in positions:
            if randrange(0, count) == 0:
                res = i
            count += 1
        return res


# Your Solution object will be instantiated and called as such:
obj = Solution([1,3,3,4,3])
for i in range(10):
    print(obj.pick(3))