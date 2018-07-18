from copy import copy
mapping = {'L':-1,'.':0,'R':1}
reverse_mapping = {-1:'L',0:'.',1:'R',-2:'L',2:'R'}
class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        l = [mapping[i] for i in dominoes]
        active = []
        for i, val in enumerate(l):
            if val != 0:
                active.append(i)
        print("".join([reverse_mapping[i] for i in l]))
        print(active)

        new_active = []
        while active:
            for i in active:
                if l[i] < 0 and i > 0 and abs(l[i-1]) != 1:
                    l[i-1] -= 2
                    new_active.append(i-1)
                if l[i] > 0 and i < len(l)-1 and abs(l[i+1]) != 1:
                    l[i+1] += 2
                    new_active.append(i+1)
            active = copy(new_active)
            new_active.clear()
            for j, val in enumerate(l):
                if val == 2:
                    l[j] = 1
                if val == -2:
                    l[j] = -1

            print("".join([reverse_mapping[i] for i in l]))
            print(active)

            


        return "".join([reverse_mapping[i] for i in l])

print(Solution().pushDominoes('.L.R...LR..L..'))
print(Solution().pushDominoes('RR.L'))
