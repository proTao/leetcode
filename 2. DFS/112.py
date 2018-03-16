from treetools import *

class Solution:
    def hasPathSum2(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        def deeper(root, current_sum):
            print(root.val,current_sum)
            if root.left is None and root.right is None:
                if current_sum == target_sum:
                    return True
                else:
                    return False

            return root.left and deeper(root.left, current_sum+root.left.val)\
                 or root.right and deeper(root.right, current_sum+root.right.val)\
                 or False

        return deeper(root, root.val)

    def hasPathSum(self, root, target_sum):
        if root == None:
            return False

        if root.left is None and root.right is None:
            if root.val == target_sum:
                return True
            return False

        return self.hasPathSum(root.left, target_sum-root.val) or\
                self.hasPathSum(root.right, target_sum-root.val)

t = stringToTreeNode("[1,2]")
prettyPrintTree(t)
print(Solution().hasPathSum(t,0))