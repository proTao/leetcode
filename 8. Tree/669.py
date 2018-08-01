from treetools import *

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if  L > R or root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, root.val-1)
            root.right = self.trimBST(root.right, root.val+1, R)
        
        return root

t = stringToTreeNode("[3]")
L = 1
R = 3
prettyPrintTree(t)
prettyPrintTree(Solution().trimBST(t,L,R))