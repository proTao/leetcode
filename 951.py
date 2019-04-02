from mytools.datastructure.treetools import *

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.flipEquiv(root1.left, root2.left) \
               and self.flipEquiv(root1.right, root2.right)\
               or self.flipEquiv(root1.left, root2.right) \
               and self.flipEquiv(root1.right, root2.left)

if __name__ == "__main__":
    t1 = stringToTreeNode("[1,2,3,4,5,6,null,null,null,7,8]")
    t2 = stringToTreeNode("[1,3,2,null,6,4,5,null,null,null,null,8,7]")
    prettyPrintTree(t1)
    prettyPrintTree(t2)
    print(Solution().flipEquiv(t1,t2))