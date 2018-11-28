from treetools import TreeNode, stringToTreeNode, prettyPrintTree
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        q1 = [root]
        q2 = []
        while q1 or q2:
            if q1:
                temp = []
                while q1:
                    node = q1.pop()
                    temp.append(node.val)
                    if node.left:
                        q2.append(node.left)
                    if node.right:
                        q2.append(node.right)
                res.append(temp)
            else:
                temp = []
                while q2:
                    node = q2.pop()
                    temp.append(node.val)
                    if node.right:
                        q1.append(node.right)
                    if node.left:
                        q1.append(node.left)
                res.append(temp)
        return res
    
t = stringToTreeNode("[]")
print(Solution().zigzagLevelOrder(t))