class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return []
        distinct_nums = set(nums)

        rest = {}
        for i in nums:
            if i in rest:
                rest[i] += 1
            else:
                rest[i] = 1
        print(rest)


        def deeper(path):
            if len(path) == len(nums):
                res.append(path)
            
            for i in distinct_nums:
                if rest[i] > 0:
                    rest[i] -= 1
                    deeper(path + [i])
                    rest[i] += 1

        deeper([])
        return res

s = Solution()
res = s.permuteUnique([1,1,2])
print(res)