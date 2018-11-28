class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r1 = len(nums)
        c1 = len(nums[0])
        if r1*c1 != r*c:
            return nums
        res = [[0 for i in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                print(str((i,j))+"->"+str(((i*c+j)/c1,(i*c+j)%c1)))
                res[i][j] = nums[(i*c+j)/c1][(i*c+j)%c1]
        return res

s=Solution()
print(s.matrixReshape([[1,2],[3,4]],4,1))
