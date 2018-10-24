class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people)-1
        res = 0
        while i < j:
            if people[i] + people[j] > limit:
                res += 1
                j -= 1
            else:
                res += 1
                j -= 1
                i += 1
        if i == j:
            res += 1
        return res

people = [3,2,2,1]
limit = 3
print(Solution().numRescueBoats(people, limit))