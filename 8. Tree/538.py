from treetools import *
class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.left == root.right == None:
            return root
        self.sum  = 0
        def visit(node):
            print("visit",node.val)
            node.val, self.sum = node.val + self.sum, self.sum + node.val

        # 中序遍历(先右后左))
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            visit(curr)
            curr = curr.left
            
        return root

        

t = stringToTreeNode("[4,2,6,1,3,5,7]")
prettyPrintTree(Solution().convertBST(t))