from treetools import *

class Solution:
    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        res = []
        if root is None:
            return res
        def deeper(path, now_sum, root):
            if root.left is None and root.right is None:
                if now_sum == target_sum:
                    res.append(path)
                return

            if root.left:
                deeper(path+[root.left.val], now_sum+root.left.val, root.left)
            if root.right:
                deeper(path+[root.right.val], now_sum+root.right.val, root.right)

        deeper([root.val], root.val, root)
        return res

t = stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
prettyPrintTree(t)
s = Solution()
res = s.pathSum(t,22)
print(res)