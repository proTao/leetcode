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
        root_i, root_j = self.root(i), self.root(j)
        if root_i != root_j:
            self.pre[root_i] = root_j
            self.components -= 1

    def componentsNum(self):
        return self.components

    def show(self):
        print(self.length, self.components)
        print(self.pre)

class DynamicUnionFind(UnionFind):
    def __init__(self, length=1):
        UnionFind.__init__(self, length)

    def add(self, i, j):
        if i >= self.length or j >= self.length:
            new_length = max(i,j) + 1
            self.components += new_length - self.length
            self.length = new_length
            self.pre += [i for i in range(len(self.pre), new_length)]

        root_i, root_j = self.root(i), self.root(j)
        if root_i != root_j:
            self.pre[root_i] = root_j
            self.components -= 1

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

'''
def DynamicUnionFind(length=1):
    components = length
    pre = [i for i in range(length)]
    def __root(i):
        # find root
        length = 0
        c = i
        while pre[i] != i:
            i = pre[i]
            length += 1
        root = i

        # path compress
        temp = pre[c]
        while temp != c:
            pre[c] = root
            c = temp
            temp = pre[c]
        return root

    def __check(i, j):
        return __root(i) == __root(j)

    def __add(i, j):
        nonlocal pre
        nonlocal components
        # expand pre
        if i >= length or j >= length:
            # raise FutureWarning("length overflow and auto expand")
            new_length = max(i,j) + 1
            components += new_length - len(pre)
            pre += [i for i in range(len(pre), new_length)]

        # add
        root_i, root_j = __root(i), __root(j)
        if root_i != root_j:
            pre[root_i] = root_j
            components -= 1
            return True
        else:
            return False

    def __count():
        return components

    def f():
        # return function object
        pass
    f.root = __root
    f.check = __check
    f.add = __add
    f.count = __count
    return f
'''

if __name__ == "__main__":
    uf = DynamicUnionFind()
    uf.add(9,10)
    uf.show()
    uf.add(8,9)
    uf.show()
    uf.add(10,1)
    uf.show()
    uf.add(8,2)
    uf.show()
