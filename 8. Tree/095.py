from treetools import *

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        self.nodes = [None] + [TreeNode(i) for i in range(1,n+1)]
        def makeTree(n, start, end):
            if n == 0:
                return [None]
            if n == 1:
                return [self.nodes[start]]
            res = []
            for left in range(0, n):
                right = n - left - 1
                root_val = start + left
                for lefttree in makeTree(left, start, root_val-1):
                    for righttree in makeTree(right, root_val+1, end):
                        root = TreeNode(root_val)
                        root.left = lefttree
                        root.right = righttree
                        res.append(root)
            return res
        return makeTree(n,1,n)

for t in Solution().generateTrees(3):
    prettyPrintTree(t)
                        
                    
                
        