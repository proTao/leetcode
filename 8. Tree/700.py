from treetools import *

class Solution:
    def searchBST(self, root:TreeNode, val:int) -> TreeNode:
        if root == None :
            return None
        
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
    
t = stringToTreeNode("[4,2,6,1,3,5,7]")
prettyPrintTree(t)
prettyPrintTree(Solution().searchBST(t, 2))