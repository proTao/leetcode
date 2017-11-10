class Solution(object):
    key_map={'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
            'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
            'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3
            }

    def word2num(self, word):
        return map(lambda x:self.key_map[x],word)

    def isInOneLine(self, word):
        word = str(word).lower()
        word = self.word2num(word)
        if word.count(word[0]) == len(word):
            return True
        else:
            return False

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = filter(self.isInOneLine, words)
        return words

s=Solution()
words = [u"Hello", u"Alaska", u"Dad", u"Peace"]
print(s.findWords(words))
