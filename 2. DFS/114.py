import treetools as tt
class Solution:
    def flatten(self, root):

        if root is None:
            return 

        def flattenCore(root):
            if root.left is None and root.right is None:
                return (root,root)


            l_head, l_tail = flattenCore(root.left) if root.left else (None, None)
                
            r_head, r_tail = flattenCore(root.right) if root.right else (None, None)

            
            root.left = None
            # print(l_head,l_tail,r_head,r_tail)
            if l_tail:
                root.right = l_head
                l_tail.right = r_head

            if r_tail is None:
                r_tail = l_tail
            return root, r_tail

        flattenCore(root)


s = Solution()
t = tt.stringToTreeNode("[1,2,null,3]")
tt.prettyPrintTree(t)
s.flatten(t)
tt.prettyPrintTree(t)