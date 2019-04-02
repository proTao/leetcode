happy_set = set()
unhappy_set = set()
def getNext(x):
    res = 0
    while x > 0:
        res += (x%10)**2
        x = x//10
    return res


class Solution:
    def isHappy(self, n: int) -> bool:
        temp_set = set()
        while True:
            if n in temp_set:
                unhappy_set.update(temp_set)
                return False
            if n in happy_set or n == 1:
                happy_set.update(temp_set)
                return True
            temp_set.add(n)
            n = getNext(n)
            print(n)

if __name__ == "__main__":
    print(Solution().isHappy(2))
    # print(getNext(19))



        