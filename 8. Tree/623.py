from treetools import *

class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newroot = TreeNode(v)
            newroot.left = root
            return newroot

        current_level = [root]
        next_level = []
        i = 2
        while i < d:
            pairs = [(i.left, i.right) for i in current_level]
            next_level = [kid for i in pairs for kid in i if kid]
            current_level = next_level
            next_level = []
            i += 1
        for node in current_level:
            left_kid = node.left
            node.left = TreeNode(v)
            node.left.left = left_kid
            right_kid = node.right
            node.right = TreeNode(v)
            node.right.right = right_kid
        return root

t = stringToTreeNode("[1,2,3,4,5,6,7]")
prettyPrintTree(t)
prettyPrintTree(Solution().addOneRow(t,1,2))