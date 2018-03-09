class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        if numRows <= 0:
            return []
        if numRows == 1:
            return res
        for x in range(2,numRows+1):
            res.append(self.get_next_layer(res[-1]))
    
        return res
        
    def get_next_layer(self, l):
        res = [l[0]]
        for i in range(len(l)-1):
            res.append(l[i]+l[i+1])
        res.append(l[-1])
        return res

s=Solution()
res = s.generate(3)
print(res)
