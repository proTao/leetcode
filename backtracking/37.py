from pprint import pprint
from random import randint
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """


        def deeper(board):
            r = randint(0,15)
            if r==0:
                pprint(board)
            (i,j) = self.getNextEmptyPosition(board)
            if i<0:
                return True
            used = {"1","2","3","4","5","6","7","8","9","."} - set(board[i]).union(set([i[j] for i in board]))\
                                    .union(self.otherFour((i,j),board))
            # print(i,j,used)
            for e in used:
                # print(i,j,used,e)
                board[i][j] = e
                if (deeper(board)):
                    return True
            board[i][j] = "."
            # print(used)

        return deeper(board)

    def otherFour(self, position, board):
        res = set()
        base_i = position[0]//3*3
        base_j = position[1]//3*3
        for i in range(base_i, base_i+3):
            for j in range(base_j, base_j+3):
                res.add(board[i][j])
        return res

    def getNextEmptyPosition(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return (i,j)
        else:
            return (-1,-1)


s = Solution()
board = [
    [".",".","9",  "7","4","8",  ".",".","."],
    ["7",".",".",  ".",".",".",  ".",".","."],
    [".","2",".",  "1",".","9",  ".",".","."],

    [".",".","7",  ".",".",".",  "2","4","."],
    [".","6","4",  ".","1",".",  "5","9","."],
    [".","9","8",  ".",".",".",  "3",".","."],

    [".",".",".",  "8",".","3",  ".","2","."],
    [".",".",".",  ".",".",".",  ".",".","6"],
    [".",".",".",  "2","7","5",  "9",".","."]
]
res = s.solveSudoku(board)
print(board)
