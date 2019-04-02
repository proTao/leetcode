from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        def gen(numRows):
            if numRows == 1:
                return [[1]]
            a = gen(numRows-1)
            layer = [1]
            for i in range(len(a)-1):
                layer.append(a[-1][i]+a[-1][i+1])
            layer.append(1)
            a.append(layer)
            return a
        return gen(numRows)

if __name__ == "__main__":
    print(Solution().generate(4))