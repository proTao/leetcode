from treetools import *

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        headnode = TreeNode(None)
        headnode.left = root
        def findnode(root_father, root, key):
            pre = root_father
            c = root
            while c and c.val != key:
                if c.val > key:
                    pre = c
                    c = c.left
                else:
                    pre = c
                    c = c.right
            if c is None:
                return None, None
            return pre, c

        def delmin(root_father, root):
            pre = root_father
            c = root
            if c.left is None:
                pre.right = c.right
            else:
                while c.left:
                    pre = c
                    c = c.left
                pre.left = c.right
            return_val = c.val
            del c
            return return_val

        def deletecore(root, key):
            pre_node, target_node = findnode(root, root.left, key)
            if target_node is None:
                return
            left = target_node.left
            right = target_node.right
            if left is None and right is None:
                if pre_node.left == target_node:
                    pre_node.left = None
                else:
                    pre_node.right = None
            elif left is None:
                if pre_node.left == target_node:
                    pre_node.left = target_node.right
                else:
                    pre_node.right = target_node.right
            elif right is None:
                if pre_node.left == target_node:
                    pre_node.left = target_node.left
                else:
                    pre_node.right = target_node.left
            else:
                target_node.val = delmin(target_node, target_node.right)

        deletecore(headnode, key)
        return headnode.left

t = stringToTreeNode("[0]")
prettyPrintTree(Solution().deleteNode(t, 0))
