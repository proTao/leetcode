from collections import namedtuple
pair = namedtuple("pair", "key value")


PERTURB_SHIFT = 5

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        类似于python的内建dict，设计本set的策略：
        1. 使用开放寻址法解决冲突
        2. 使用与python内部一致的二次哈希函数
        3. 桶个数每次加倍
        4. 负载因子的阈值设置为2/3
        5. 因为元素都是数字，所以使用字符串“duumy”表示dummy态的桶
        """
        self.mask = 7
        self.used = 0
        self.filled = 0
        self.data = [None for i in range(self.mask+1)]
        
    def search(self, key):
        # 最后可以直接使用的位置
        freeslot = None

        # 首次寻址
        i = key & self.mask
        if self.data[i] is None:
            return i
        elif self.data[i] is 'dummy':
            freeslot = i
        elif self.data[i].key == key:
            return i
        else:
            pass
        
        # 开放寻址
        perturb = key
        data = self.data
        while True:
            i = (i << 2) + i + perturb + 1
            i = i & self.mask
            slot = data[i]
            if slot is None:
                return freeslot if freeslot else i
            if isinstance(slot, pair) and slot.key == key:
                return i
            if slot is "dummy" and freeslot is None:
                freeslot = i

            perturb >>= PERTURB_SHIFT
        
    def put(self, key: int, value: int) -> None:
        self.insert(key, value)
        if self.filled / (self.mask + 1) >= 2/3:
            self.resize()

    def insert(self, key: int, value:int) -> None:
        # 相比于add，不会resize
        # 被add和resize所调用
        i = self.search(key)
        slot = self.data[i]
        if slot is None:
            self.data[i] = pair(key, value)
            self.used += 1
            self.filled += 1
        elif slot is "dummy":
            self.data[i] = pair(key, value)
            self.used += 1
        else: # slot.key == key
            if slot.value != value:
                self.data[i] = pair(key, value)
        

    def remove(self, key: int) -> None:
        i = self.search(key)
        slot = self.data[i]
        if isinstance(slot, pair) and slot.key == key:
            self.data[i] = "dummy"
            self.used -= 1
            if self.filled / (self.used + 1) >= 3:
                self.resize()
        

    def __contains__(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.data[self.search(key)].key == key
    
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        slot = self.data[self.search(key)]
        if isinstance(slot, pair) and slot.key == key:
            return slot.value
        else:
            return -1

    def resize(self):
        # 使得 newsize 保证是2的整数次幂
        newsize_upperbound = self.used*4 if self.used<100 else self.used*2
        newsize = 1
        while newsize <= newsize_upperbound:
            newsize <<= 1
        newsize = max(8, newsize)
        
        if newsize == self.mask+1:
            return

        oldtable = self.data
        self.data = [None] * newsize
        self.mask = newsize - 1
        self.filled = 0
        self.used = 0
        for slot in oldtable:
            if isinstance(slot, pair):
                self.insert(slot.key, slot.value)

    def showState(self):
        print("used:{} filled:{} capacity:{}".format(self.used, self.filled, self.mask+1))
        print("loading rate =", self.filled/(self.mask+1))
        print(self.data)

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class OthersHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 5000
        self.h = [None] * self.m


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ind = key % self.m
        if self.h[ind] == None:
            self.h[ind] = ListNode(key, value)
        else:
            cur = self.h[ind]
            while cur and cur.key != key:
                prev = cur
                cur = cur.next
            if key == self.h[ind].key:
                self.h[ind].val = value
            else:
                prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ind = key % self.m
        cur = self.h[ind]
        while cur and cur.key != key:
            cur = cur.next
        if cur == None:
            return -1
        else:
            return cur.val


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ind = key % self.m
        cur = self.h[ind]
        if cur and cur.key == key:
            self.h[ind] = cur.next
        else:
            while cur and cur.key != key:
                prev = cur
                cur = cur.next
            if cur != None:
                prev.next = cur.next



if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1,1)
    obj.put(2,2)
    obj.get(1)
    obj.get(3)
    obj.put(2,1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))

