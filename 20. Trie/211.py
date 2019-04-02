def helper(trie, subfix):
    if subfix == "":
        return "" in trie
    c = subfix[0]
    if c == ".":
        return any(helper(trie[i], subfix[1:]) for i in trie if i != "")
    else:
        return c in trie and helper(trie[c], subfix[1:])

class WordDictionary:
    def __init__(self):
        self.trie = {}
    
    def addWord(self, word):
        p = self.trie
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p[""] = None
    
    def search(self, word):
        return helper(self.trie, word)

if __name__ == "__main__":
    """
    ["search","search","search","search","search"]
[["a"],["aa"],["a"],[".a"],["a."]]
    """
    t = WordDictionary()
    t.addWord('a')
    t.addWord('a')
    print(t.search("."))
    print(t.search("a."))
    print(t.search(".a"))
