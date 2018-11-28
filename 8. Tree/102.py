from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q1 = deque([root])
        q0 = deque()
        flag = True
        current_q = q1 if flag else q0
        next_q = q1 if not flag else q0
        res = []
        while current_q:
            temp = []
            while current_q:
                node = current_q.popleft()
                temp.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            flag = not flag
            current_q = q1 if flag else q0
            next_q = q1 if not flag else q0
            res.append(temp)
        return res

