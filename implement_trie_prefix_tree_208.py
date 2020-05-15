'''
208. Implement Trie (Prefix Tree)
Medium

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

https://leetcode.com/problems/implement-trie-prefix-tree/
'''
class Node:
    def __init__(self):
        self.next = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for char in word:
            curr = ord(char) - ord('a')
            if not root.next[curr]:
                root.next[curr] = Node()
            root = root.next[curr]
        root.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for char in word:
            curr = ord(char) - ord('a')
            if not root.next[curr]:
                return False
            root = root.next[curr]
        if root.isEnd:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for char in prefix:
            curr = ord(char) - ord('a')
            if not root.next[curr]:
                return False
            root = root.next[curr]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
