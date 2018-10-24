from treetools import *

class Solution:
    def diameterOfBinaryTree(self, root:TreeNode)->int:

        def deeper(root:TreeNode)->tuple:
            """
            rtype:(start with root, diameter)
            """
            if root is None:
                return (0,1)
            else:
                l = deeper(root.left)
                r = deeper(root.right)
                return 1+max(l[0],r[0]), max((1+l[0]+r[0],l[1],r[1]))
        return deeper(root)[1]-1

t = stringToTreeNode("[1]")
prettyPrintTree(t)
print(Solution().diameterOfBinaryTree(t))