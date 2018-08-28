class Trie:

    _end = '_end'
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        trie = self.trie
        for char in word:
            trie = trie.setdefault(char, {})
        trie.setdefault(self._end, self._end)
        
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie = self.trie
        for char in word:
            trie = trie.get(char)
            if trie is None:
                return False
        return bool(trie.get(self._end))
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        trie = self.trie
        for char in prefix:
            trie = trie.get(char)
            if trie is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

