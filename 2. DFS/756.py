from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.allowed = defaultdict(lambda : [])
        for i in allowed:
            self.allowed[i[:2]].append(i[2])


        print(self.allowed)

        self.find_solution = False
        def deeper(bottom, path, layer):
            print(bottom, path, layer)
            if len(path) == layer:
                if layer == 1:
                    self.find_solution = True
                else:
                    deeper(path, "", layer-1)


            [deeper(bottom, path+i, layer) \
                    for i in self.allowed[bottom[len(path):len(path)+2]] \
                    if not self.find_solution]
                   


        deeper(bottom, "", len(bottom)-1)
        return self.find_solution



s = Solution()
bottom = "ABCD"
allowed = ["BCE","BCF","ABA","CDA","AEG","FAG","GGG"]
res = s.pyramidTransition(bottom, allowed)
print(res)