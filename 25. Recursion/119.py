from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def core(k):
            if k == 0:
                return [1]
            a = core(k-1)
            for i in range(len(a)-1, 0, -1):
                a[i] = a[i]+a[i-1]
            a.append(1)
            return a
        return core(rowIndex)

if __name__ == "__main__":
    print(Solution().getRow(1))