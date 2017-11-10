import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        self.store = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dictionary:
            return False
        else:
            if len(self.store) == self.length:
                self.store.append(val)
            else:
                self.store[self.length] = val
            self.dictionary[val] = self.length
            self.length += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dictionary:
            remove_index = self.dictionary[val]
            self.store[remove_index] = self.store[self.length-1]
            self.dictionary[self.store[self.length-1]] = remove_index
            self.length -= 1
            self.dictionary.pop(val)
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.length == 0:
            return False
        index = random.randint(0,self.length-1)
        return self.store[index]

    def show(self):
        print("length : "+str(self.length))
        print(self.store)
        print(self.dictionary)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
obj = RandomizedSet()
print(obj.insert('a'))
obj.show()
print(obj.insert('b'))
obj.show()
print(obj.insert('c'))
obj.show()
print(obj.insert('d'))
obj.show()
print(obj.remove('b'))
obj.show()
print(obj.getRandom())
