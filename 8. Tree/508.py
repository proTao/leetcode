from treetools import *

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.val2count = {}
        def core(node : TreeNode):
            if node.left is None and node.right is None:
                node_val = node.val
            else:
                left_val = core(node.left) if node.left else 0
                right_val = core(node.right) if node.right else 0
                node_val = node.val + left_val + right_val
            if node_val not in self.val2count:
                self.val2count[node_val] = 1
            else:
                self.val2count[node_val] += 1
            return node_val
        core(root)
        # print(self.val2count)
        res = []
        max_count = max(self.val2count.values())
        for i,j in self.val2count.items():
            if j == max_count:
                res.append(i)
        return res

t = stringToTreeNode("[1,2,-1]")            
print(Solution().findFrequentTreeSum(t))


        

                