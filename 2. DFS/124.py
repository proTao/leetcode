from treetools import *
from pprint import pprint
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathSumCore(root):
            # return (the path must from root to leaf, no constrant)
            if root.left is None and root.right is None:
                return (root.val, root.val)

            l_root = l_any = r_root = r_any = -1000000
            if root.left:
                l_root, l_any = maxPathSumCore(root.left)
            if root.right:
                r_root, r_any = maxPathSumCore(root.right)
            root_root = max(l_root, r_root) + root.val
            root_any = max(l_any, r_any, root.val + l_root + r_root)
            print(root_root, root_any)
            return root_root, root_any

        return max(maxPathSumCore(root))

t = stringToTreeNode("[2,-1]")
prettyPrintTree(t)
s = Solution()
print(s.maxPathSum(t))

