class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

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



class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        for i, j in zip(treeLeafIterator(root1), treeLeafIterator(root2)):
            if i != j:
                return False
        return True
    


def treeLeafIterator(t):

    def deeper(node):
        if node.left is None and node.right is None:
            yield node.val

        if node.left:
            yield from deeper(node.left)

        if node.right:
            yield from deeper(node.right)

    yield from deeper(t)


t1 = stringToTreeNode("[3,5,1,6,2,9,8,null,null,7,4]")
t2 = stringToTreeNode("[3,5,1,3,4,9,3,6,7,null,null,null,null,null,9]")
print(Solution().leafSimilar(t1,t2))