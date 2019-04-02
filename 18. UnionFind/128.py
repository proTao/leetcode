from typing import List

class UnionFindNode:
    def __init__(self, data_=None):
        self.data = data_
        self.parent = None
        self.size = 1

class LinkedUnionFind():
    def __init__(self):
        self.length = 0
        self.components = 0 # 连通组分个数
        self.maxComponentsSize = 0 # 最大连通组分的大小
        self.size = 0 # 节点数
        self.index = {} # 将index映射为data的下标，间接寻址
        self.data = [] # 存放UnionFindNode的数组

    def find(self, i):
        # find root
        node = self.data[self.index[i]]
        p = node.parent
        length = 1

        while p is not None:
            if p.parent:
                # path compress
                node.parent = p.parent
            node = p
            p = p.parent
            length += 1
        root = node

        # path compress
        # node = self.data[self.index[i]]
        # p = node.parent
        # while p is not None:
        #     node.parent = root
        #     node = p
        #     p = node.parent
        return root

    def isConnect(self, i, j):
        return self.root(i) is self.root(j)

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.components -= 1
            if root_i.size < root_j.size:
                root_i.parent = root_j
                root_j.size += root_i.size
                if root_j.size > self.maxComponentsSize:
                    self.maxComponentsSize = root_j.size
                root_i.size = -1
            else:
                root_j.parent = root_i
                root_i.size += root_j.size
                if root_i.size > self.maxComponentsSize:
                    self.maxComponentsSize = root_i.size
                root_j.size = -1


    def add(self, index):
        if index in self.index:
            return False
        else:
            self.size += 1
            temp = UnionFindNode(index)
            self.data.append(temp)
            self.index[index] = self.size-1
            self.components += 1
            if self.maxComponentsSize == 0:
                self.maxComponentsSize = 1
            return True



class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        uf = LinkedUnionFind()
        for i in nums:
            uf.add(i)
            if i-1 in uf.index:
                uf.union(i-1, i)
            if i+1 in uf.index:
                uf.union(i+1, i)
        return uf.maxComponentsSize

if __name__ == "__main__":
    l = [-1, 1, 0]
    print(Solution().longestConsecutive(l))