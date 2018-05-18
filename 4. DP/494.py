class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # remove zeros
        i = 0
        zeros = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                nums = nums[:i] + nums[i+1:]
                i -= 1 
                length -= 1
                zeros += 1
            i += 1
        
        # all elements is zeros
        if len(nums) == 0:
            if S == 0:
                return 2**zeros
            else:
                return 0

        # accumulate
        acc = [0] * (length + 1)
        for i in range(length):
            acc[i+1] = acc[i] + nums[i]

        self.cache = {}

        def deeper(j, S, t=0):
            # print("\t"*t,nums[0:j+1],S)
            # this operation can be remove
            # because the "elif" statement below can do the same thing
            # if i == j:
            #     return int(nums[j]==abs(S))
            if (j,S) in self.cache:
                return self.cache[(j,S)]

            local_sum = acc[j+1]
            if local_sum < abs(S):
                # print("\t"*t,nums[0:j+1],(0,j),S,"=>",0)
                res = 0
            elif local_sum == abs(S):
                # print("\t"*t,nums[0:j+1],(0,j),S,"=>",1)
                res = 1
            else:
                res = deeper(j-1,S-nums[j]) + deeper(j-1,S+nums[j])

                # print("\t"*t,nums[0:j+1],(0,j),S,"=>",res)
            self.cache[(j,S)] = res
            return res
        
        return deeper(length-1,S) * 2 ** zeros


s = Solution()
print(s.findTargetSumWays([6,44,30,25,8,26,34,22,10,18,34,8,0,32,13,48,29,41,16,30],12))