from treetools import *

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.makeZeroNone(root)
        def core(root):
            if root.left:
                if root.left.val is None:
                    del root.left
                    root.left = None
                else:
                    core(root.left)
            if root.right:
                if root.right.val is None:
                    del root.right
                    root.right = None
                else:
                    core(root.right)
        core(root)
        return root       

        

    def makeZeroNone(self, root:TreeNode):
        if root.left is None:
            left_zero_flag = True
        else:
            left_zero_flag = self.makeZeroNone(root.left)
        
        if root.right is None:
            right_zero_flag = True
        else:
            right_zero_flag = self.makeZeroNone(root.right)

        if left_zero_flag and right_zero_flag and root.val == 0:
            root.val = None
            return True
        return False


t = stringToTreeNode("[1,0,1,0,0,0,1]")
prettyPrintTree(Solution().pruneTree(t))
