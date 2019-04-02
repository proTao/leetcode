class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        maxnum = nums[0]
        maxindex = 0
        enough_large = True
        for i, cur in enumerate(nums[1:], start=1):
            if cur > maxnum:
                enough_large = cur >= maxnum * 2
                maxnum = cur
                maxindex = i
            else:
                enough_large = enough_large and maxnum >= cur * 2
        return maxindex if enough_large else -1

if __name__ == "__main__":
    a = [0,2,3,0]
    print(Solution().dominantIndex(a))