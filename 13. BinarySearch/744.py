class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # letters is sorted

        l = 0
        r = len(letters)
        while l < r:
            mid = (l + r)//2
            if letters[mid] < target:
                l = mid + 1
            elif letters[mid] > target:
                if r > mid + 1:
                    r = mid + 1
                else:
                    break
            else:
                l = mid + 1

        for i in range(l, r):
            if letters[i] > target:
                return letters[i]
        return letters[0]


print(Solution().nextGreatestLetter([1,2,3,4,6,6], 6))