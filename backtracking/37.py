import time
from random import randint
from pprint import pprint
USE_HUMAN_EXPERIENCE = True


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if USE_HUMAN_EXPERIENCE:
            self.priorty = {}
            for i in range(21):
                self.priorty[i] = []

            self.updatePriority(board)
            

        
        def deeper(board):
            # outputToFile(board)
            # if USE_HUMAN_EXPERIENCE:
            #     r = randint(1,20)
            #     if r == 1:
            #         self.updatePriority(board)

            ((i,j),p) = self.getNextEmptyPosition(board)
            print(i,j,p)
            # print(i,j,p)
            if i<0:
                return True
            not_used = {"1","2","3","4","5","6","7","8","9","."} - set(board[i]).union(set([i[j] for i in board]))\
                                    .union(set(self.otherFourElement((i,j),board)))
            # print(i,j,used)
            for e in not_used:
                # print(i,j,used,e)
                board[i][j] = e
                if (deeper(board)):
                    return True
            else:
                board[i][j] = "."


            if USE_HUMAN_EXPERIENCE:
                # self.updatePriority(board)
                self.priorty[p].append((i,j))
            # print(self.priorty)
                
            # print(used)

        deeper(board)

    def otherFourElement(self, position, board):
        res = []
        base_i = position[0] // 3 * 3
        base_j = position[1] // 3 * 3
        for i in range(base_i, base_i+3):
            for j in range(base_j, base_j+3):
                if i == position[0] or j == position[1]:
                    continue
                res.append(board[i][j])
        return res

    def getNextEmptyPosition(self, board):
        if USE_HUMAN_EXPERIENCE:
            for i in range(21):
                if len(self.priorty[i]) > 0:
                    return (self.priorty[i].pop(),i)

        else:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return ((i,j),None)
            
        return ((-1,-1),None)

    def updatePriority(self, board):
        # print("update priority")
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    p = board[i].count(".") \
                        + [i[j] for i in board].count(".") \
                        + self.otherFourElement((i,j),board).count(".") -2
                    self.priorty[p].append((i,j))
        pprint(self.priorty)


def outputToFile(board):
    time.sleep(0.03)
    with open("output","w") as f:
        
        
        f.writelines(board[0][0:3]+[" "]+board[0][3:6]+[" "]+board[0][6:9]+["\n"])
        f.writelines(board[1][0:3]+[" "]+board[1][3:6]+[" "]+board[1][6:9]+["\n"])
        f.writelines(board[2][0:3]+[" "]+board[2][3:6]+[" "]+board[2][6:9]+["\n"])
        f.writelines("\n")
        f.writelines(board[3][0:3]+[" "]+board[3][3:6]+[" "]+board[3][6:9]+["\n"])
        f.writelines(board[4][0:3]+[" "]+board[4][3:6]+[" "]+board[4][6:9]+["\n"])
        f.writelines(board[5][0:3]+[" "]+board[5][3:6]+[" "]+board[5][6:9]+["\n"])
        f.writelines("\n")
        f.writelines(board[6][0:3]+[" "]+board[6][3:6]+[" "]+board[6][6:9]+["\n"])
        f.writelines(board[7][0:3]+[" "]+board[7][3:6]+[" "]+board[7][6:9]+["\n"])
        f.writelines(board[8][0:3]+[" "]+board[8][3:6]+[" "]+board[8][6:9]+["\n"])







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
pprint(board)
# print(s.priorty)