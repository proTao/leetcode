class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = None

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.children:
                for i in curr.children[::-1]:
                    stack.append(i)
        return res




n=[0]
for i in range(1,7):
    n.append(Node(i))

n[1].children=[n[3],n[2],n[4]]
n[3].children=[n[5],n[6]]
t = n[1]
print(Solution().preorder(t))