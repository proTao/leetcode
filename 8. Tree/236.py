from treetools import *

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.q_find = False
        self.q_find = False
        self.flag = 0 # 0:not find; 1:find p; 2:find q; 3:find both
        self.p = p
        self.q = q
        self.res = None

        def find(root):
            if self.flag == 3:
                return
            node_find = 0
            if root is self.p:
                node_find = 1
            elif root is self.q:
                node_find = 2

            left_res = find(root.left) if root.left else 0
            right_res = find(root.right) if root.right else 0
            current_res = node_find | left_res | right_res
            if current_res == 3 and self.res is None:
                self.res = root
                self.flag == 3
            return current_res
        find(root)
        return self.res
            
root = stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
p = 5
q = 1
print(Solution().lowestCommonAncestor(root,p,q))