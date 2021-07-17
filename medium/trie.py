class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        i = 0
        cur = self.root
        while i < len(word):
            char = word[i]
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            i += 1
        cur.endOfWord = True



        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        i = 0
        cur = self.root
        while i < len(word):
            char = word[i]
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            i += 1
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        i = 0
        cur = self.root
        while i < len(word):
            char = word[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            i += 1
            
        return cur.endOfWord:
             
                
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        i = 0
        cur = self.root
        while i < len(prefix):
            char = prefix[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            i += 1
        return True
        