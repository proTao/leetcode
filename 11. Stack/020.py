class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = set(('(','[','{'))
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if stack:
                    cand = stack.pop()
                    if cand == '(' and c == ')' or\
                        cand == '[' and c == ']' or\
                        cand == '{' and c == '}':
                        continue
                return False
        if stack:
            return False
        return True

print(Solution().isValid("]"))
