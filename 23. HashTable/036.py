from typing import List

def getGridKey(i, j):
    if i<3 and j<3:
        return 0
    if 3<=i<6 and j<3:
        return 1
    if i>=6 and j<3:
        return 2
    if i<3 and 0<=j<6:
        return 3
    if 3<=i<6 and 0<=j<6:
        return 4
    if i>=6 and 0<=j<6:
        return 5
    if i<3 and j>=6:
        return 6
    if 3<=i<6 and j>=6:
        return 7
    if i>=6 and j>=6:
        return 8

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [None] + [set() for _ in range(9)] # row_set[i]表示数字i出现在过第几行
        col_set = [None] + [set() for _ in range(9)]
        grid_set = [None] + [set() for _ in range(9)]
        for i, line in enumerate(board):
            for j, x in enumerate(line):
                if x == ".":
                    continue
                else:
                    x = int(x)
                # print(i,j)
                if i in row_set[x]:
                    return False
                else:
                    row_set[x].add(i)

                if j in col_set[x]:
                    return False
                else:
                    col_set[x].add(j)
                
                k = getGridKey(i,j)
                if k in grid_set[x]:
                    return False
                else:
                    grid_set[x].add(k)
            
        return True

if __name__ == "__main__":
    a = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(Solution().isValidSudoku(a))