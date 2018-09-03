class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return "Treenode "+str(self.val)

        
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

def PostOrderTraversal(root:TreeNode):
    if root is None:
        raise StopIteration
    stack = [root]
    curr = None
    pre = None
    while stack:
        curr = stack[-1]
        if curr.left == curr.right == None or\
            pre and (pre == curr.left or pre == curr.right):
            yield curr
            stack.pop()
            pre = curr
        else:
            curr.right and stack.append(curr.right)
            curr.left and stack.append(curr.left)

def InOrderTraversal(root:TreeNode, returnval=True):
    if root is None:
        raise StopIteration
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if returnval:
            yield curr.val
        else:
            yield curr
        curr = curr.right

def PreOrderTraversal(root:TreeNode, returnval=True):
    if root is None:
        raise StopIteration
    stack = [root]
    while stack:
        curr = stack.pop()
        if returnval:
            yield curr.val
        else:
            yield curr

        curr.right and stack.append(curr.right)
        curr.left and stack.append(curr.left)

def LevelOrderTraversal(root:TreeNode, bylevel=True):
    if root is None:
        raise StopIteration
    layer0 = [root]
    layer1 = []
    trigger = 0
    current_layer = layer1 if trigger else layer0
    next_layer = layer0 if trigger else layer1

    while current_layer:
        if bylevel:
            level = []
        for i in current_layer:
            if bylevel:
                level.append(i.val)
            else:
                yield i.val
            i.left and next_layer.append(i.left)
            i.right and next_layer.append(i.right)
        if bylevel:
            yield level

        current_layer.clear()
        trigger = 1 - trigger
        current_layer = layer1 if trigger else layer0
        next_layer = layer0 if trigger else layer1        

if __name__ == "__main__":
    t = stringToTreeNode("[1,2,3,4,5,6,7]")
    prettyPrintTree(t)
    for i in PostOrderTraversal(t):
        print(i)
