from treetools import *

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.res = 0
        def deeper(root:TreeNode, is_left):
            if root.left:
                deeper(root.left, True)
            if root.right:
                deeper(root.right, False)
            if root.left is None and root.right is None and is_left:
                self.res += root.val
        deeper(root, False)
        return self.res

t = stringToTreeNode("[1]")
prettyPrintTree(t)
print(Solution().sumOfLeftLeaves(t))     
        