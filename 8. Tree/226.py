from treetools import *

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

t = stringToTreeNode("[1,2,3,4,5,6,7,8,null,9,null]")
prettyPrintTree(t)
prettyPrintTree(Solution().invertTree(t))
