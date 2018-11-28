from treetools import *

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = float("inf")
        second_min = float("inf")
        for i in InOrderTraversal(root):
            print(i,min_val, second_min)
            if i < min_val:
                second_min = min_val
                min_val = i
            elif min_val < i < second_min:
                second_min = i
        return -1 if second_min == float("inf") else second_min

t = stringToTreeNode("[2,2,2,null,null,2,3]")
prettyPrintTree(t)
print(Solution().findSecondMinimumValue(t))