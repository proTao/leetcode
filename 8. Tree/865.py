from treetools import *

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.depth = 0
        self.deep_node_count = 0

        def getAllDeepest(root, depth):
            if depth > self.depth:
                self.depth = depth
                if root.left is None and root.right is None:
                    self.deep_node_count = 1
            elif depth == self.depth:
                if root.left is None and root.right is None:
                    self.deep_node_count += 1
            else:
                pass

            root.left and getAllDeepest(root.left, depth+1)
            root.right and getAllDeepest(root.right, depth+1)
        getAllDeepest(root, 1)
        print(self.depth, self.deep_node_count)
        self.stopflag = False
        self.res = None
        def getSubTree(root, depth):
            # stop situation
            if root.left is None and root.right is None:
                node_count =  1 if depth == self.depth else 0
            else:
                # recursion
                left_count = getSubTree(root.left, depth+1) if root.left else 0
                right_count = getSubTree(root.right, depth+1) if root.right else 0
                if self.stopflag:
                    return
                node_count = left_count + right_count
            if node_count == self.deep_node_count:
                self.stopflag = True
                self.res = root
            else:
                return node_count
        getSubTree(root,1)
        return self.res

t = stringToTreeNode("[1]")
prettyPrintTree(t)
prettyPrintTree(Solution().subtreeWithAllDeepest(t))

            