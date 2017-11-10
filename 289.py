class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.height = len(board)
        self.width = len(board[0])
        if self.width + self.height <= 3:
            for i in range(self.height):
                for j in range(self.width):
                    board[i][j] = 0
        else:
            self.next_state = [[0 for i in range(self.width)] for j in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    if board[i][j] + self.getNeightbor(i,j,board) == 3 \
                        or board[i][j] == 1 and self.getNeightbor(i,j,board) == 3:
                        self.next_state[i][j] = 1
                        print(i,j)
            for i in range(self.height):
                for j in range(self.width):
                    board[i][j] = self.next_state[i][j]

    def getNeightbor(self,i,j,board):
        count = 0
        # single line
        if i == 0 and self.height == 1:
            if j == 0:
                return board[0][1]
            if j == self.width-1:
                return board[0][j-1]
            return board[0][j-1]+board[0][j+1]
        if j == 0 and self.width == 1:
            if i == 0:
                return board[1][0]
            if i == self.height-1:
                return board[i-1][0]
            return board[i-1][0]+board[i+1][0]


        # corner
        if i == 0 and j == 0:
            return board[1][1] + board[1][0] + board[0][1]
        if i == 0 and j == self.width-1:
            return board[0][j-1] + board[1][j-1] + board[1][j]
        if i == self.height-1 and j == 0:
            return board[i][1] + board[i-1][0] + board[i-1][1]
        if i == self.height-1 and j == self.width-1:
            return board[i-1][j-1] + board[i-1][j] + board[i][j-1]


        # border
        if i == 0:
            return board[i][j-1]+board[i][j+1]+board[i+1][j]+board[i+1][j-1]+board[i+1][j+1]
        if i == self.height-1:
            return board[i][j-1]+board[i][j+1]+board[i-1][j]+board[i-1][j-1]+board[i-1][j+1]
        if j == 0:
            return board[i-1][j]+board[i+1][j]+board[i-1][j+1]+board[i][j+1]+board[i+1][j+1]
        if j == self.width-1:
            return board[i-1][j]+board[i+1][j]+board[i-1][j-1]+board[i][j-1]+board[i+1][j-1]

        return board[i][j-1]+board[i][j+1]+board[i-1][j]+board[i-1][j-1]+board[i-1][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]





s=Solution()

s.gameOfLife([[1,1],[1,0]])
