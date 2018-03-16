# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None :
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1+self.minDepth(root.right)
        if root.right is None:
            return 1+self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth(self, root):
        self.min_depth = 10000000
        if root == None:
            return 0

        def deeper(root, current_depth):
            print(root.val)
            if root.left == None and root.right == None:
                if current_depth < self.min_depth:
                    self.min_depth = current_depth
                return

            if current_depth + 1 < self.min_depth:
                if root.left:
                    deeper(root.left, current_depth+1)
                if root.right:
                    deeper(root.right, current_depth+1)

        deeper(root, 1)
        return self.min_depth

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

print("res",Solution().minDepth(stringToTreeNode("[1,null,2]")))