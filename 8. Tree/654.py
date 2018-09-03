from treetools import *

class Solution:
    def constructMaximumBinaryTree(self, nums):
        def core(l:list):
            if len(l) == 1:
                return TreeNode(l[0])

            maxelement = max(l)
            maxindex = l.index(maxelement)
            node = TreeNode(maxelement)
            if maxindex > 0:
                node.left = core(l[:maxindex])
            if maxindex < len(l) - 1:
                node.right = core(l[maxindex+1:])
            return node
        
        return core(l)


l = [3, 2, 1, 6, 0, 5]
prettyPrintTree(Solution().constructMaximumBinaryTree(l))