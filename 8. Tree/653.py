from treetools import *

class Solution():
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False

        # one pass by hashtable
        hashtable = set()
        # dfs by stack
        stack = [root]

        while stack:
            print(stack, hashtable)
            node = stack.pop()
            node.left and stack.append(node.left)
            node.right and stack.append(node.right)
            if node.val in hashtable:
                return True
            else:
                hashtable.add(k - node.val)
        return False

t = stringToTreeNode("[5,3,6,2,4,null,7]")
prettyPrintTree(t)
print(Solution().findTarget(t, 9))

