from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+':lambda x,y:x+y, 
                      '-':lambda x,y:x-y,
                      '*':lambda x,y:x*y,
                      '/':lambda x,y:int(x/y)} # different with x//y
        for i in tokens:
            if i in operations:
                right = stack.pop()
                left = stack.pop()
                stack.append(operations[i](left, right))
            else:
                stack.append(int(i))
        return stack[0]

if __name__ == "__main__":
    a = ["2", "1", "+", "3", "*"]
    a = ["4", "13", "5", "/", "+"]
    a = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(a))