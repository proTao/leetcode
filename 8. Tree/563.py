from treetools import *

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.res = 0
        def deeper(root:TreeNode) -> int:
            if root is None:
                return 0
            lsum = deeper(root.left)
            rsum = deeper(root.right)
            self.res += abs(lsum - rsum)
            print(root, lsum, rsum, self.res)
            return lsum + rsum + root.val
        
        lsum = deeper(root.left)
        rsum = deeper(root.right)
        self.res += abs(lsum - rsum)
        return self.res
            
t = stringToTreeNode("[1,2,3,4,null,5]")
prettyPrintTree(t)
print(Solution().findTilt(t))