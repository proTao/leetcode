from treetools import *

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.find_p = False
        self.find_q = False
        self.p_path = None
        self.q_path = None
        def searchPandQ(path):
            curr = path[-1]
            if self.find_p and self.find_q:
                return
            if not self.find_p and curr is p:
                self.p_path = path.copy()
                self.find_p = True
            if not self.find_q and curr is q:
                self.q_path = path.copy()
                self.find_q = True
            if curr.left:
                searchPandQ(path+[curr.left])
            if curr.right:
                searchPandQ(path+[curr.right])
        searchPandQ([root])
        print(self.p_path)
        print(self.q_path)
        min_l = min(len(self.p_path), len(self.q_path))
        if self.p_path[min_l-1] is self.q_path[min_l-1]:
            return self.q_path[min_l-1]
        for i in range(min_l):
            print(i)
            if not self.p_path[i] is self.q_path[i]:
                break
        return self.q_path[i-1]

t = stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]")
prettyPrintTree(t)
print(Solution().lowestCommonAncestor(t, t.left, t.left.right))




        