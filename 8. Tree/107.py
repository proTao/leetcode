from treetools import *

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        for i in LevelOrderTraversal(root):
            res.append(i)
        return res[::-1]
t = stringToTreeNode("[3,9,20,null,null,15,7]")
prettyPrintTree(t)
print(Solution().levelOrderBottom(t))
