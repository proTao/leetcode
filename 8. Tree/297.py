from treetools import *

from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        output = []
        while q:
            node = q.popleft()
            if isinstance(node, TreeNode):
                output.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                output.append("x")
        return ",".join(output)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        q = deque([])
        if data[0] is 'x':
            return None
        q.append(TreeNode(data[0]))
        root = q[0]
        for i in range(len(data)//2):
            if data[1+(i<<1)] != 'x':
                leftnode = TreeNode(int(data[1+(i<<1)]))
                q.append(leftnode)
            else:
                leftnode = None
            if data[2+(i<<1)] != 'x':
                rightnode = TreeNode(int(data[2+(i<<1)]))
                q.append(rightnode)
            else:
                rightnode = None

            node = q.popleft()
            node.left = leftnode
            node.right = rightnode

        return root


        

# Your Codec object will be instantiated and called as such:
t = stringToTreeNode("[1,2,null,3,null,4,5]")
prettyPrintTree(t)
codec = Codec()
s = codec.serialize(t)
print(s)
prettyPrintTree(codec.deserialize(s))