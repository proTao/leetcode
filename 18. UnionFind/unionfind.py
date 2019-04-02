class UnionFind():
    def __init__(self, length):
        self.length = length
        self.components = length
        self.pre = [i for i in range(length)]

    def root(self, i):
        # find root
        length = 0
        c = i
        while self.pre[i] != i:
            i = self.pre[i]
            length += 1
        root = i

        # path compress
        temp = self.pre[c]
        while temp != c:
            self.pre[c] = root
            c = temp
            temp = self.pre[c]
        return root

    def isConnect(self, i, j):
        return self.root(i) == self.root(j)

    def union(self, i, j):
        # print(i,j)
        root_i, root_j = self.root(i), self.root(j)
        if root_i != root_j:
            self.pre[root_i] = root_j
            self.components -= 1
        return 

    def componentsNum(self):
        return self.components

    def show(self):
        print(self.length, self.components)
        print(self.pre)

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
            # if p.parent:
            #     # path compress
            #     node.parent = p.parent
            node = p
            p = p.parent
            length += 1

        return node.data
    
    def path(self, i):
        node = self.data[self.index[i]]
        p = node.parent
        length = 1
        res = [node.data]
        while p is not None:
            # if p.parent:
            #     # path compress
            #     node.parent = p.parent
            res.append(p.data)
            node = p
            p = p.parent
            length += 1
        return res

    def isConnect(self, i, j):
        return self.find(i) is self.find(j)

    def union(self, i, j):
        """
        return: 哪个元素的根发生变动
        """
        root_i = self.data[self.index[self.find(i)]]
        root_j = self.data[self.index[self.find(j)]]
        if root_i != root_j:
            self.components -= 1
            if root_i.size < root_j.size:
                root_i.parent = root_j
                root_j.size += root_i.size
                if root_j.size > self.maxComponentsSize:
                    self.maxComponentsSize = root_j.size
                root_i.size = -1
                return i, root_i.data, root_j.data
            else:
                root_j.parent = root_i
                root_i.size += root_j.size
                if root_i.size > self.maxComponentsSize:
                    self.maxComponentsSize = root_i.size
                root_j.size = -1
                return j, root_i.data, root_j.data
        return None, None, None

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
    
    def __contains__(self, index):
        return index in self.index