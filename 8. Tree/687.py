from treetools import *

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def deeper(root):
            """
            return (from root, any path)
            """
            if root.left is None and root.right is None:
                return (1,1)
            r1=r2=1
            if root.left:
                l = deeper(root.left)
                if root.left.val == root.val:
                    r1 = l[0] + 1
                    r2 = l[0] + 1
            else:
                l = (0,0)
            if root.right:
                r = deeper(root.right)
                if root.right.val == root.val:
                    r1 = max(r1, r[0] + 1)
                    r2 += r[0]
            else:
                r = (0,0)
            r2 = max(l[1],r[1],r2)
            print(root, (r1, r2))
            return r1,r2
        return deeper(root)[1]-1
        
t = stringToTreeNode("[5,4,5,1,1,5]")
prettyPrintTree(t)
print(Solution().longestUnivaluePath(t))