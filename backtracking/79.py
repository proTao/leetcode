LEFT = 0
RIGHT = 3
UP = 1
DOWN = 2

DEBUG = False

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.height = len(board)
        if self.height == 0:
            return False

        self.width = len(board[0])
        if self.height * self.width < len(word):
            return False


        def deeper(path, last_direction = -1):
            """
            path:list of tuple, the tuple is the position index of each step
            """

            # return confition
            if len(path) == len(word):
                print(path)
                return True

            # deeper to each branch
            current_position = path[-1]
            if DEBUG:
                print()
                print("current_position", current_position)

            condition_UP = last_direction != DOWN and current_position[0]-1 >= 0 and \
                board[current_position[0]-1][current_position[1]] == word[len(path)] and \
                ((current_position[0]-1,current_position[1]) not in path)
            

            condition_DOWN = last_direction != UP and current_position[0]+1 <= self.height-1 and \
                board[current_position[0]+1][current_position[1]] == word[len(path)] and \
                ((current_position[0]+1,current_position[1]) not in path)
                

            condition_LEFT = last_direction != RIGHT and current_position[1]-1 >= 0 and \
                board[current_position[0]][current_position[1]-1] == word[len(path)] and \
                ((current_position[0],current_position[1]-1) not in path)
                

            condition_RIGHT = last_direction != LEFT and current_position[1]+1 <= self.width-1 and \
                board[current_position[0]][current_position[1]+1] == word[len(path)] and \
                ((current_position[0],current_position[1]+1) not in path)
            
            if DEBUG:
                print(condition_UP,condition_DOWN,condition_LEFT,condition_RIGHT)

            return condition_UP and deeper(path + [(current_position[0]-1, current_position[1])], UP) or \
                    condition_DOWN and deeper(path + [(current_position[0]+1, current_position[1])], DOWN) or \
                    condition_LEFT and deeper(path + [(current_position[0], current_position[1]-1)], LEFT) or \
                    condition_RIGHT and deeper(path + [(current_position[0], current_position[1]+1)], RIGHT) or \
                    False


        for i in range(self.height):
            for j in range(self.width):
                if board[i][j] == word[0]:
                    if DEBUG:
                        print("start from", (i,j))

                    res = deeper([(i,j)])
                    if res:
                        return True

        return False

s = Solution()
b = [
["a","a","a"],
["a","b","b"],
["a","b","b"],
["b","b","b"],
["b","b","b"],
["a","a","a"],
["b","b","b"],
["a","b","b"],
["a","a","b"],
["a","b","a"]
]
w = "aabaaaabbb"
print(s.exist(b,w))