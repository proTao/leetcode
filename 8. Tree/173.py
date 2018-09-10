# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

def BSTIterator(root):
    stack = []
    curr = root
    def next():
        nonlocal curr
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res = curr.val
            curr = curr.right
            return res
    def hasNext():
        return not curr is None or len(stack) > 0
    def core():
        pass
    core.__call__ = None
    core.next = next
    core.hasNext = hasNext
    return core


        

# Your BSTIterator will be called like this:
root = stringToTreeNode("[4,2,6,1,3,5,7]")

it = BSTIterator(root)
while it.hasNext():
    print(it.next())