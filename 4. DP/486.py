class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        memo = {}

        for i in range(len(nums)-1):
            memo[(i,i+1)] = abs(nums[i]-nums[i+1])
            print(memo[(i,i+1)], end=" ")
        print()

        for delta in range(2, len(nums)):
            for i in range(len(nums)-delta):
                memo[(i,i+delta)] = max(nums[i] - memo[(i+1,i+delta)],\
                                        nums[i+delta] - memo[(i, i+delta-1)])
                print(memo[(i, i+delta)], end=" ")
            print()

        return memo[(0,len(nums)-1)] >= 0


s = Solution()
print(s.PredictTheWinner([1,5,3,7,4,6,2]))