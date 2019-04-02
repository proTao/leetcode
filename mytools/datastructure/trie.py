class Trie:
    def __init__(self, end=""):
        self.trie = {}
        self.end_symbol = end
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.trie
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p[self.end_symbol]=None
    
    def _walk_to(self, path:str) -> dict:
        """
        walk in the trie
        :type word: str
        :rtype: None od dict
        """
        p = self.trie
        for c in path:
            if c not in p:
                return None
            p = p[c]
        return p

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self._walk_to(word)
        return p is not None and self.end_symbol in p

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self._walk_to(prefix)
        return p is not None and len(p) > 0
