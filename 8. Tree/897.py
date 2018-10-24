from treetools import *

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = None
        node = None
        for i in self.preorder(root):
            if res is None:
                res = TreeNode(i.val)
                node = res
            else:
                node.right = TreeNode(i.val)
                node = node.right
        return res

    def preorder(self, root):
        node = root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node
            node = node.right

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.res = root
        while self.res.left:
            self.res = self.res.left

        def changeOrder(node):
            if node.left is None and node.right is None:
                return node

            if node.right:
                node.right = changeOrder(node.right)

            if node.left:
                left = node.left
                node.left = None
                new_pre = changeOrder(left)
                new_pre.right = node
                return new_pre
            else:
                return node
        
        changeOrder(root)
        return self.res
             


t = stringToTreeNode("[5,3,6,2,4,null,8,1,null,null,null,7,9]")
prettyPrintTree(t)
prettyPrintTree(Solution().increasingBST(t))