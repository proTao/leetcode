from pprint import pprint
class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.height = len(board)
        self.width = len(board[0])
        self.visited = [[False for i in range(len(board))] for j in range(len(board[0]))]
        self.board = board
        def deeper(x, y):
            if 0<=(x)<self.height and 0<=(y)<self.width:
                if self.board[x][y] == 'M':
                    self.board[x][y] = 'X'

                if self.board[x][y] == 'E':
                    mines = self.countNeighborMines(x,y)
                    if mines > 0:
                        self.board[x][y] = str(mines)
                    else:
                        self.board[x][y] = "B"
                        deeper(x-1,y-1)
                        deeper(x-1,y)
                        deeper(x-1,y+1)
                        deeper(x,y-1)
                        deeper(x,y+1)
                        deeper(x+1,y-1)
                        deeper(x+1,y)
                        deeper(x+1,y+1)

        deeper(click[0], click[1])
        return self.board

    def countNeighborMines(self,x,y):
        count = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0<=(x+i)<self.height and \
                    0<=(y+j)<self.width and \
                    self.board[x+i][y+j] == "M":
                    count += 1
        return count

s = Solution()
board = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]

pprint(board)
board = s.updateBoard(board, [0,0])
pprint(board==[["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]])
# board = s.updateBoard(board, [0,2])
