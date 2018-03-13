class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        nums.sort()

        def deeper(path, start_position):
            # print(path, start_position)
            # return condition
            res.append(path)

            # go deeper
            last_element = None
            for i in range(start_position, len(nums)):
                if last_element != nums[i]:
                    deeper(path+[nums[i]], i+1)
                    last_element = nums[i]

        
        deeper([],0)
        return res

s = Solution()
res = s.subsetsWithDup([2,1,2])
print()
print(res)