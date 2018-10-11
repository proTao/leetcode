class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        current_score = 0

        for c in S:
            if c is "(":
                stack.append(c)
            else:
                x = stack.pop()
                while x != "(":
                    current_score += x
                    x = stack.pop()
                if current_score == 0:
                    stack.append(1)
                else:
                    stack.append(2*current_score)
                current_score = 0
        return sum(stack)
s = "()"
print(Solution().scoreOfParentheses(s))