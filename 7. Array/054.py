from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        position_i = position_j = 0
        d = 0 # diretion flag
        up_bound = -1
        left_bound = -1
        down_bound = len(matrix)
        right_bound = len(matrix[0])
        res = [0] * (down_bound*right_bound)
        index = 0
        while down_bound-up_bound>1 and right_bound-left_bound>1:
            res[index] = matrix[position_i][position_j]
            index += 1
            if d == 0: # go right now
                if position_j+1 == right_bound:
                    d = 1
                    position_i += 1
                    up_bound += 1
                else:
                    position_j += 1
            elif d == 1: # go down now
                if position_i+1 == down_bound:
                    d = 2
                    position_j -= 1
                    right_bound -= 1
                else:
                    position_i += 1
            elif d == 2: # go left now
                if position_j-1 == left_bound:
                    d = 3
                    position_i -= 1
                    down_bound -= 1
                else:
                    position_j -= 1
            else: # go up now
                if position_i-1 == up_bound:
                    d = 0
                    position_j += 1
                    left_bound += 1
                else:
                    position_i -= 1
        return res

if __name__ == "__main__":
    a = [[1],[2],[3]]
    print(Solution().spiralOrder(a))