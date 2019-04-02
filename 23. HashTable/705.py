PERTURB_SHIFT = 5

class MyHashSet:

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
        if self.data[i] is None or \
           self.data[i] == key:
            return i
        elif self.data[i] is 'dummy':
            freeslot = i
        else:
            pass
        
        # 开放寻址
        perturb = key
        data = self.data
        cnt = 0
        while True:
            if cnt > self.mask:
                print(data)
                assert False
            cnt += 1
            i = (i << 2) + i + perturb + 1
            i = i & self.mask
            if data[i] is None:
                return freeslot if freeslot else i
            if data[i] == key:
                return i
            if data[i] is "dummy" and freeslot is None:
                freeslot = i

            perturb >>= PERTURB_SHIFT

        
    def add(self, key: int) -> None:
        self.insert(key)
        if self.filled / (self.mask + 1) >= 2/3:
            self.resize()


    def insert(self, key: int) -> None:
        # 相比于add，不会resize
        # 被add和resize所调用
        i = self.search(key)
        if self.data[i] == key:
            return
        else:
            if self.data[i] is None:
                self.data[i] = key
                self.used += 1
                self.filled += 1
            else: #"dummy"
                self.data[i] = key
                self.used += 1



    def remove(self, key: int) -> None:
        i = self.search(key)
        if self.data[i] == key:
            self.data[i] = "dummy"
            self.used -= 1
            if self.filled / (self.used + 1) >= 3:
                self.resize()
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.data[self.search(key)] == key
    
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
        for key in oldtable:
            if isinstance(key, int):
                self.insert(key)

    def showState(self):
        print("used:{} filled:{} capacity:{}".format(self.used, self.filled, self.mask+1))
        print("loading rate =", self.filled/(self.mask+1))
        print(self.data)

class OtherHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.size = 1000
        self.data = [None] * self.size
        

    def add(self, key: int) -> None:
        index = key % self.size
        if self.data[index] is not None:
            if key not in self.data[index]:
                self.data[index].append(key)
        else:
            self.data[index] = [key]
        #print("add",self.data)

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.data[index] is not None:
            if key in self.data[index]:
                self.data[index].remove(key)
        #print("remove",self.data)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        if self.data[index] is not None:
            return key in self.data[index]
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
import random
l = [4378, 2305, 1794, 4611, 298, 5, 2810, 129, 1364, 2348, 58, 3339, 2107, 2434, 63, 15, 2320, 1553, 4626, 1027, 2474, 2842, 2838, 2583, 1538, 25, 282, 315, 3612, 2333, 1310, 4101, 1125, 3105, 546, 1827, 291, 37, 2598, 4778, 4150, 2857, 554, 4907, 1836, 3762, 558, 4221, 2404, 3889, 1596, 4881, 365, 4661, 677, 2185, 3128, 1081, 1338, 479, 1084, 317, 830, 1589, 3340, 4929, 1562, 3381, 1679, 837, 3306, 3770, 2692, 2377, 1866, 951, 332, 2381, 2638, 2127, 4944, 4945, 2559, 3939, 3668, 14, 4299, 3641, 3376, 857, 4427, 1187, 2140, 3677, 3678, 101, 2039, 3088, 4769, 611, 2390, 4197, 2662, 2407, 1640, 2977, 618, 2535, 2126, 1680, 2414, 4709, 4785, 3432, 4452, 4716, 495, 2110, 4130, 3571, 4777, 3449, 2345, 3195, 4377, 4733, 1785, 1582, 2944, 2433, 386, 619, 1412, 4741, 162, 4599, 2408, 340, 1145, 2808, 2674, 1068, 3214, 911, 2663, 276, 3218, 403, 2196, 1685, 3478, 4121, 1829, 1184, 1690, 2715, 156, 154, 329, 2885, 3270, 3233, 2466, 3491, 3492, 4517, 2470, 1447, 1448, 1770, 1283, 711, 4312, 4386, 3638, 309, 1054, 3077, 313, 57, 1899, 862, 694, 695, 3300, 1012, 4538, 31, 1724, 2749, 608, 237, 4281, 2241, 3079, 963, 4763, 4209, 3014, 4513, 1224, 4553, 4298, 203, 2530, 3277, 4558, 463, 4806, 3962, 3538, 2259, 4820, 1959, 1942, 2809, 4200, 1828, 4857, 731, 4828, 4832, 4062, 4575, 736, 3691, 3065, 2531, 337, 4774, 230, 3047, 1559, 764, 4330, 1003, 3425, 4333, 3929, 613, 2439, 753, 4850, 1501, 4084, 3198, 2782, 2601, 3609, 4089, 477, 3067, 2300, 1066, 3326, 3327]
for i in l:
    obj.add(i)
obj.showState()
