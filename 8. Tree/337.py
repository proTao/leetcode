from treetools import *

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def core(root):
            if root is None:
                return 0, 0
            else:
                theft_left, not_theft_left = core(root.left)
                theft_right, not_theft_right = core(root.right)
                theft_this = root.val + not_theft_left + not_theft_right
                not_theft_this = max(theft_left, not_theft_left) +\
                                 max(theft_right, not_theft_right)
                return theft_this, not_theft_this
        return max(core(root))

t = stringToTreeNode("[3,4,5,1,3,null,1]")
print(Solution().rob(t))