from copy import copy

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        layer0 = [root]
        layer1 = []
        trigger = 0
        current_layer = layer1 if trigger else layer0
        next_layer = layer0 if trigger else layer1
        while current_layer:
            for i in current_layer:
                i.children and next_layer.extend(i.children)
            res.append([i.val for i in current_layer])
            trigger = 1 - trigger
            current_layer = layer1 if trigger else layer0
            next_layer = layer0 if trigger else layer1
            for i in range(len(next_layer)):
                next_layer.pop()
        return res

n=[0]
for i in range(1,7):
    n.append(Node(i))

n[1].children=[n[3],n[2],n[4]]
n[3].children=[n[5],n[6]]

print(Solution().levelOrder(n[1]))
        