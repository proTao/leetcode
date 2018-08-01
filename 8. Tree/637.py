from treetools import *

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        layer0 = [root]
        layer1 = []
        trigger = 0
        current_layer = layer1 if trigger else layer0
        next_layer = layer0 if trigger else layer1
        res = []
        while current_layer:
            for i in current_layer:
                i.left and next_layer.append(i.left)
                i.right and next_layer.append(i.right)
            res.append(sum(i.val for i in current_layer)/len(current_layer))
            current_layer.clear()
            trigger = 1 - trigger
            current_layer = layer1 if trigger else layer0
            next_layer = layer0 if trigger else layer1
        return res

t = stringToTreeNode("[3,9,20,null,null,15,7]")
prettyPrintTree(t)
print(Solution().averageOfLevels(t))