from collections import defaultdict
import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(set)
        self.store = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # is exist?
        if val in self.dic and len(self.dic[val])>0:
            res = False
        else:
            res = True

        # store 
        if self.length < len(self.store):
            self.store[self.length] = val
        else:
            self.store.append(val)
        self.dic[val].add(self.length)
        self.length += 1

        # record the index
        self.dic[val].add(self.length-1)

        return res


    def remove(self, val):
        """
        Remove a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic and len(self.dic[val])>0:
            # modify store
            index = self.dic[val].pop()
            last_element = self.store[self.length-1]
            self.store[index]=last_element
            
            #modify index
            self.dic[last_element].add(index)
            self.dic[last_element].remove(self.length-1)

            self.length -= 1
            return True
        else:

            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randint(0,self.length-1)
        return self.store[index]

    def show(self):
        print("length : "+str(self.length))
        print(self.store)
        print(self.dic)
        print()

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

obj = RandomizedCollection()
obj.insert(1)
obj.show()
# obj.insert(2)
# obj.show()
# obj.insert(3)
# obj.show()
# obj.insert(1)
# obj.show()
obj.remove(1)
obj.show()
obj.insert(1)
obj.show()
# obj.remove(3)
# obj.show()