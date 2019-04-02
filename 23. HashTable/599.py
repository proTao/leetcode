from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {}
        for i, x in enumerate(list1):
            map1[x] = i
        
        minsum = 10000
        restaurant = []
        for i, x in enumerate(list2):
            if x in map1:
                j = map1[x]
                if i + j < minsum:
                    minsum = i+j
                    restaurant = [x]
                elif i + j == minsum:
                    restaurant.append(x)
                else:
                    pass
        return restaurant

if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(Solution().findRestaurant(list1, list2))