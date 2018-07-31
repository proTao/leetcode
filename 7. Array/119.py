class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        # becasue i think the top layer is layer 1
        # but in the problem , the top layer in layer 0
        rowIndex = rowIndex+1
        if rowIndex <= 0:
            return []

        res = [1]
        if rowIndex == 1:
            return res
        

        for i in range(2, rowIndex+1):
            res.append(1)
            for j in range(i-2, 0,-1):
                # print(j)
                # print(res)

                res[j] = res[j] + res[j-1]
                
            # print("layer", i,res)

        return res
s = Solution()
res = s.getRow(9)
print(res)
