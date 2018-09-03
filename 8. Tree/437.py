from treetools import *

class Solution:
    def pathSum(self, root:TreeNode, sum:int)->int:

        if root is None:
            return 0
        return self.pathSumFrom(root, sum) +\
                self.pathSum(root.left, sum) +\
                self.pathSum(root.right, sum)
    
    
    def pathSumFrom(self,node:TreeNode, sum:int):
        if node is None:
            return 0
        return (1 if node.val == sum else 0) +\
                self.pathSumFrom(node.left, sum - node.val) +\
                self.pathSumFrom(node.right, sum - node.val);
    

t = stringToTreeNode("[10,5,-3,3,2,null,11,3,-2,null,1]")
prettyPrintTree(t)

print(Solution().pathSum(t,8))
        