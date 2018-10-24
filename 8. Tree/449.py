from treetools import *

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def preorder(root):
            serialization = []
            stack = [root]
            node = None
            while stack:
                node = stack.pop()
                serialization.append(str(node.val))
                node.right and stack.append(node.right)
                node.left and stack.append(node.left)
            return serialization

        def inorder(root):
            serialization = []
            stack = []
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                serialization.append(str(node.val))
                node = node.right
            return serialization
        if root is None:
            return []
        return preorder(root) + inorder(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data[:len(data)//2]
        inorder = data[len(data)//2:]
        def reconstruct(preorder, inorder:list):
            if len(preorder) == 0:
                return None

            root = TreeNode(preorder[0])
            i = inorder.index(root.val)
            left_in_order = inorder[:i]
            right_in_order = inorder[i+1:]
            left_pre_order = preorder[1:i+1]
            right_pre_order = preorder[i+1:]
            root.left = reconstruct(left_pre_order, left_in_order)
            root.right = reconstruct(right_pre_order, right_in_order)
            return root

        return reconstruct(list(map(int, preorder)), list(map(int, inorder)))

# Your Codec object will be instantiated and called as such:
root = stringToTreeNode("[]")
codec = Codec()
s = codec.serialize(root)
print(s)
prettyPrintTree(codec.deserialize(s))
