class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return board

        self.height = len(board)
        self.width = len(board[0])

        def deeper(i, j, board):
            if 0<=i<self.height and 0<=j<self.width and board[i][j]=="O":
                board[i][j] = "0"

                deeper(i-1, j, board)
                deeper(i+1, j, board)
                deeper(i, j-1, board)
                deeper(i, j+1, board)

        for i in range(self.height):
            deeper(i, 0, board)
            deeper(i, self.width-1, board)

        for i in range(self.width):
            deeper(0, i, board)
            deeper(self.height-1, i, board)

        for i in range(self.height):
            for j in range(self.width):
                if board[i][j] == '0':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X' 

from pprint import pprint
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
res = Solution().solve(board)
pprint(board)