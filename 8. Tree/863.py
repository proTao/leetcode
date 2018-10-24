from treetools import *

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.res = []
        def search(root, path, K, top):
            # top表示有没有可能root是path的祖先
            if top and len(path) == K and K > 0:
                self.res.append(root.val)
            if path == '':
                if K == 0:
                    self.res.append(root.val)
                else:
                    root.left and search(root.left, path, K-1, False)
                    root.right and search(root.right, path, K-1, False)
            else:
                next_step = path[0]
                if next_step == 'L':
                    root.right and search(root.right, "", K-len(path)-1, False)
                    root.left and search(root.left, path[1:], K, top)
                else: # R
                    root.left and search(root.left, "", K-len(path)-1, False)
                    root.right and search(root.right, path[1:], K, top)
        search(root, self.getPath(target, root, ''), K, True)
        return self.res

    def getPath(self, target, root, path):
        if target is root:
            return path
        elif root is None:
            return None
        else:
            res = self.getPath(target, root.left, path + 'L')
            if res:
                return res
            else:
                return self.getPath(target, root.right, path + 'R')
    

        

root = stringToTreeNode("[0,2,1,null,null,3]")
prettyPrintTree(root)
target = root.right.left
print(Solution().distanceK(root, target, 3))