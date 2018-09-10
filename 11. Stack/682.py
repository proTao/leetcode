class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        current_sum = 0
        for op in ops:
            if op == "C":
                score = stack.pop()
                current_sum -= score
            elif op == "D":
                stack.append(stack[-1] * 2)
                current_sum += stack[-1]
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
                current_sum += stack[-1]
            else:
                stack.append(int(op))
                current_sum += stack[-1]
            # print(stack, current_sum)
        return current_sum

a =  ["5","2","C","D","+"] # 30
# a = ["5","-2","4","C","D","9","+","+"] # 27
print(Solution().calPoints(a))