class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return []

        visited = {i:False for i in nums}
        
        def deeper(path):
            if len(path) == len(nums):
                res.append(path)
            
            for i in nums:
                if not visited[i]:
                    visited[i] = True
                    deeper(path + [i])
                    visited[i] = False

        deeper([])
        return res

s = Solution()
print(s.permute([1,2]))