class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        # assume nums is already sorted

        def deeper(path, index):
            # path是当前搜索的路径
            # i是下一个要被加入进路径的位置值
            # print(path, index)
            res.append(path)

            for i in range(index, len(nums)):
                deeper(path+[nums[i]], i+1)

        deeper([],0)

        return res
    def subset2():

        
s = Solution()
res = s.subsets([1,2,3,4])
print(len(res))


