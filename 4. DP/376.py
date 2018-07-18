class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        new_nums = [nums[0]]
        last_i = nums[0]
        for i in nums:
            if i == last_i:
                continue
            else:
                new_nums.append(i)
                last_i = i
        nums = new_nums
        if len(nums) <= 1:
            return len(nums)


        dp = [(True, float("-inf"))] * len(nums)
        dp[1] = (nums[1] > nums[0], 2)
        for i, n in enumerate(nums):
            if i < 2: 
                continue
            print(i,n)
            max_l = float("-inf")
            for j in range(i-1, 0, -1):
                if (nums[i] > nums[j]) ^ dp[j][0] and dp[j][1] >= max_l:
                    flag = nums[i] > nums[j]
                    max_l = dp[j][1] + 1
                    break
            try:
                dp[i] = (flag, max_l)
            except UnboundLocalError as e:
                print("bad")
                dp[i] = (nums[i] > nums[0], 2)
            print(dp)
        
        return dp[-1][1]

a=[2,4,5,7,5,5,7,1,2,3]
print(Solution().wiggleMaxLength(a))

