class Solution:
    def totalNQueens(self, n):
        self.res = 0

        # direction of diag1 is \, direction of diag2 is /
        def deeper(path, vertical, diag1, diag2):
            if len(path) == n:
                self.res += 1
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
        return self.res

s=Solution()
res = s.totalNQueens(4)
print(res)