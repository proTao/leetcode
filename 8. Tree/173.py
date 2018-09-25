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

class BSTIterator():
    def __init__(self, root):
        self.stack = []
        self.curr = root
    def next(self):
        while self.curr or self.stack:
            while self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            self.curr = self.stack.pop()
            res = self.curr.val
            self.curr = self.curr.right
            return res
    def hasNext(self):
        return not self.curr is None or len(self.stack) > 0
    
    
    
    
    
        

# Your BSTIterator will be called like this:
root = stringToTreeNode("[4,2,6,1,3,5,7]")

it = BSTIterator(root)
while it.hasNext():
    print(it.next())