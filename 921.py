from collections import deque

# class Solution:
#     def minAddToMakeValid(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
#         l = deque(list(S))
#         count = 0
#         res = 0
#         while l:
#             if len(l) == 1:
#                 res += 1
#                 break
#             elif l[0] == '(' and l[-1] == ')':
#                 l.pop()
#                 l.popleft()
#                 count += 1
#             elif l[0] == ')' and l[-1] == '(':
#                 l.pop()
#                 l.popleft()
#                 if count >= 1:
#                     count -= 1
#                 else:
#                     res += 2
#             elif l[0] == l[-1]:
#                 res += 1
#                 if l[0] == '(':
#                     l.append(')')
#                 else:
#                     l.appendleft("(")
#         return res
class Solution:
    def minAddToMakeValid(self, S):
        left = 0
        right = 0
        for c in S:
            if c == "(":
                right += 1
            if c == ")":
                if right > 0:
                    right -= 1
                else:
                    left += 1
        return left + right
print(Solution().minAddToMakeValid("()))(("))