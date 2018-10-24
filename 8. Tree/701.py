from treetools import *

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(root, val):
            root_val = root.val
            if root_val < val:
                if root.right:
                    insert(root.right, val)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    insert(root.left, val)
                else:
                    root.left = TreeNode(val)
        insert(root, val)
        return root
            