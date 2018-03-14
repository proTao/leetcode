from pprint import pprint
DEBUG = True

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["." for i in range(n)] for j in range(n)]
        visited = [[0 for i in range(n)] for j in range(n)]
        res = []

        def deeper(index1):
            if index1 == n:
                if DEBUG:
                    print("-----------solution!--------")
                    pprint(board)
                temp = []
                for i in board:
                    temp.append("".join(i))
                res.append(temp)
                return 

            for index2 in range(n):
                # print(index1,index2)
                if visited[index1][index2] == 0:
                    # prepare
                    board[index1][index2] = "Q"
                    visited[index1][index2] -= 3
                    for i in range(n):
                        visited[index1][i] += 1
                        visited[i][index2] += 1
                    ## LU:left up point,LD:left Down point
                    LU_1 = index1 - min(index1, index2)
                    LU_2 = index2 - min(index1, index2)
                    LD_1 = index1 + min(n - 1 - index1, index2)
                    LD_2 = index2 - min(n - 1 - index1, index2)
                    for i in range(n - max(LU_1, LU_2)):
                        visited[LU_1 + i][LU_2 + i] += 1
                    for i in range(n - max(n - 1 - LD_1, LD_2)):
                        visited[LD_1 - i][LD_2 + i] += 1

                    if DEBUG:
                        print("put down", index1, index2)
                        pprint(board)
                        for i in visited:
                            print(i)

                    # deeper
                    deeper(index1 + 1)

                    # recover
                    board[index1][index2] = "."
                    visited[index1][index2] += 3
                    for i in range(n):
                        visited[index1][i] -= 1
                        visited[i][index2] -= 1
                    ## LU:left up point,LD:left Down point
                    LU_1 = index1 - min(index1, index2)
                    LU_2 = index2 - min(index1, index2)
                    LD_1 = index1 + min(n - 1 - index1, index2)
                    LD_2 = index2 - min(n - 1 - index1, index2)
                    for i in range(n - max(LU_1, LU_2)):
                        visited[LU_1 + i][LU_2 + i] -= 1
                    for i in range(n - max(n - 1 - LD_1, LD_2)):
                        visited[LD_1 - i][LD_2 + i] -= 1

                    if DEBUG:
                        print("put up", index1, index2)
                        pprint(board)
                        for i in visited:
                            print(i)


        deeper(0)
        return res

    def solveNQueens2(self, n):

        res = []

        def deeper(path):
            if DEBUG:
                for i in path:
                    print(i)
                print()

            if len(path) == n:
                res.append(path)
                return 

            # try to put nect queen on board[index1][index2]
            index1 = len(path)
            for index2 in range(n):
                if DEBUG:
                    print("test on",index1,index2)

                # judge if this branch is possible
                condition = True

                ## just up direction
                for i in range(len(path)):
                    if path[i][index2] == "Q":
                        condition = False

                ## up and left direction
                if condition:
                    LU_1 = index1 - min(index1, index2)
                    LU_2 = index2 - min(index1, index2)
                    for i in range(min(len(path), index2)):
                        if path[LU_1 + i][LU_2 + i] == "Q":
                            condition= False

                ## up and right direction
                if condition:
                    RU_1 = index1 - min(index1, n - 1 - index2)
                    RU_2 = index2 + min(index1, n - 1 - index2)
                    for i in range(min(len(path), n - 1 - index2)):
                        if path[RU_1 + i][RU_2 - i] == "Q":
                            condition= False

                if condition:
                    if DEBUG:
                        print("put down on %i,%i" % (index1, index2))
                    deeper(path+["."*index2+"Q"+"."*(n-1-index2)])
                    if DEBUG:
                        print("put up from %i,%i" % (index1, index2))
                

        deeper([])
        return res

    def solveNQueens3(self, n):
        res = []

        # direction of diag1 is \, direction of diag2 is /
        def deeper(path, vertical, diag1, diag2):
            if len(path) == n:
                res.append(path)
                return 

            index1 = len(path)
            for index2 in range(n):
                index_on_diag1 = n-1-index1+index2
                index_on_diag2 = index1+index2
                if not vertical[index2] and not diag1[index_on_diag1] and not diag2[index_on_diag2]:
                    deeper(path+["."*index2+"Q"+"."*(n-1-index2)],
                           vertical[:index2]+[True]+vertical[index2+1:],
                           diag1[:index_on_diag1]+[True]+diag1[index_on_diag1+1:],
                           diag2[:index_on_diag2]+[True]+diag2[index_on_diag2+1:],
                           )
        deeper([], [False for i in range(n)], [False for i in range(2*n-1)], [False for i in range(2*n-1)])
        return res

    def solveNQueens4(self, n):
        res = []
        vertical = [False for i in range(n)]
        diag1 = [False for i in range(2*n-1)]
        diag2 =  [False for i in range(2*n-1)]
        # direction of diag1 is \, direction of diag2 is /
        def deeper(path):
            if len(path) == n:
                res.append(path)
                return 

            index1 = len(path)
            for index2 in range(n):
                index_on_diag1 = n-1-index1+index2
                index_on_diag2 = index1+index2
                if not vertical[index2] and not diag1[index_on_diag1] and not diag2[index_on_diag2]:
                    vertical[index2] = True
                    diag1[index_on_diag1] = True
                    diag2[index_on_diag2] = True
                    deeper(path+["."*index2+"Q"+"."*(n-1-index2)])
                    vertical[index2] = False
                    diag1[index_on_diag1] = False
                    diag2[index_on_diag2] = False
        deeper([])
        return res


s=Solution()
res = s.solveNQueens4(4)

pprint(res)




    
