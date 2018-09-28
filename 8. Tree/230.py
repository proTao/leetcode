from treetools import *

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.count = 1
        return self.inorder(root, self.visit)
        
    def inorder(self, root, visit):
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if visit(node):
                return node.val
            node = node.right
    
    def visit(self, n: TreeNode):
        if self.count == self.k:
            return True
        else:
            self.count += 1
            return False



t = stringToTreeNode("[5,2,6,1,4,null,7,null,null,3]")
# prettyPrintTree(t)
for i in range(7):
    print(Solution().kthSmallest(t, i))