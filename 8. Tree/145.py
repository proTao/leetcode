from treetools import *

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def postorder(root):
            stack = []
            node = root
            pre = None

            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack[-1]
                if node.right is None or node.right is pre:
                    self.res.append(node.val)
                    pre = stack.pop()
                    node = None
                else:
                    node = node.right
        postorder(root)
        return self.res

t = stringToTreeNode("[1,2,11,3,7,12,4,5,8,9,null,null,null,null,null,6,null,null,null,10]")
prettyPrintTree(t)
print(Solution().postorderTraversal(t))