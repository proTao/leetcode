from treetools import *

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.largest = []
        if root is None:
            return self.largest
        def deeper(root, depth):
            if depth > len(self.largest):
                self.largest.append(root.val)
            else:
                if root.val > self.largest[depth-1]:
                    self.largest[depth-1] = root.val

            if root.left:
                deeper(root.left, depth+1)
            if root.right:
                deeper(root.right, depth+1)

        deeper(root, 1)
        return self.largest





t = stringToTreeNode("[]")
prettyPrintTree(t)
print(Solution().largestValues(t))
        