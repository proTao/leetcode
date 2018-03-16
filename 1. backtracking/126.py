from pprint import pprint
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """


        res = []
        self.word_length = len(beginWord)
        self.buildConnectionMappping(beginWord, wordList)
        self.shortest_path_length = self.findShortestPath(beginWord, endWord, wordList)
        print(self.shortest_path_length)
        
        # 用candidate，空间换时间
        def deeper(path, candidates):
            # print(path,candidates)
            if path[-1] == endWord:
                res.append(path)
                return

            if len(path) < self.shortest_path_length:
                for i in range(len(candidates)):
                    for j in range(self.word_length):
                        if path[-1][j] != candidates[i][j]:
                            break
                    if path[-1][j+1:] == candidates[i][j+1:]:
                        deeper(path + [candidates[i]], candidates[0:i]+candidates[i+1:])

        deeper([beginWord], wordList)
        return res

    def findShortestPath(self, beginWord, endWord, wordList):
        current_layer = [beginWord]
        next_layer = []
        visited = set()
        not_find_end_word = True
        count = 1

        while current_layer and not_find_end_word:
            # print(current_layer)
            count += 1
            for word in current_layer:
                print("Asd",word)
                for next_word in self.mapping[word]:
                    if next_word == endWord:
                        not_find_end_word = False
                    if next_word not in visited:
                        visited.add(next_word)
                        next_layer.append(next_word)
            current_layer = next_layer
            next_layer = []
        return count

            

    def buildConnectionMappping(self, beginWord, wordList):
        # can not from word (in wordList) to beginWord
        wordList.sort()
        self.mapping = defaultdict(lambda :[])
        for i in range(0,len(wordList)):
            for j in range(i+1,len(wordList)):
                for k in range(self.word_length):
                    if wordList[i][k] != wordList[j][k]:
                        break
                if wordList[i][k+1:] == wordList[j][k+1:]:
                    self.mapping[wordList[i]].append(wordList[j])
                    self.mapping[wordList[j]].append(wordList[i])

        for w in wordList:
            print(w)
            for k in range(self.word_length):
                if w[k] != beginWord[k]:
                    break
            if w[k+1:] == beginWord[k+1:]:
                self.mapping[beginWord].append(w)

        


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = s.findLadders(beginWord, endWord, wordList)
pprint(res)



