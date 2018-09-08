from collections import defaultdict

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # s1= "ab" s2 = "eidboaoo"
        table1 = defaultdict(lambda: 0)
        table2 = defaultdict(lambda: 0)
        if len(s1) > len(s2):
            return False
        for c1,c2 in zip(s1, s2):
            table1[c1] += 1
            table2[c2] += 1
        
        match_count = 0
        for c in 'qwertyuiopasdfghjklzxcvbnm':
            if table1[c] == table2[c]:
                match_count += 1
        i = 0
        j = len(s1)
        while j < len(s2):
            if match_count == 26:
                return True
            
            if table1[s2[i]] == table2[s2[i]]:
                match_count -= 1
            if table1[s2[j]] == table2[s2[j]]:
                match_count -= 1

            table2[s2[i]] -= 1
            table2[s2[j]] += 1
            if table1[s2[i]] == table2[s2[i]]:
                match_count += 1
            if table1[s2[j]] == table2[s2[j]]:
                match_count += 1


            i += 1
            j += 1
        if match_count == 26:
            return True
        return False


s1= "abc"
s2 = "eidboacboo"
s1 = "adc"
s2 = "dcda"
# s1 = "hello"
# s2 = "ooolleoooleh"
# s1 = "abc"
# s2 = "ccccbbbbaaaa"

print(Solution().checkInclusion(s1,s2))