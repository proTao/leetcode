from collections import Counter
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies_count = Counter(candies)
        print(candies_count, len(candies_count))
        return min(len(candies_count), len(candies)//2)

candies = [1,1,1,1,2,2,2,3,3,3]
print(Solution().distributeCandies(candies))