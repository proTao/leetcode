class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.depth = 0
        if root is None:
            return 0

        def deeper(root, depth):
            if depth > self.depth:
                self.depth = depth
            for i in root.children:
                deeper(i, depth + 1)
        deeper(root, 1)
        return self.depth