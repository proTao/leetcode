class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(",")
        stack = [preorder[0]]
        pop_num = 0
        if preorder[0] == "#":
            if len(preorder) == 1:
                return True
            else:
                return False
        for c in preorder[1:]:
            if len(stack) == 0:
                return False
            if c != "#":
                stack.append(c)
            else:
                pop_num += 1
            while pop_num >= 2:
                if stack:
                    stack.pop()
                    pop_num -= 1
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

s = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# s = "1,#,#,1"
s = "20,10,7,4,#,#,8,#,#,14,#,#,30,25,#,#,40,#,#"
print(Solution().isValidSerialization(s))