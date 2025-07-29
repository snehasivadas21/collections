class Trienode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=Trienode()
    def insert(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=Trienode()
            cur=cur.children[char]
        cur.is_end=True
    def search(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return cur.is_end
    def prefix(self,prefix):
        cur=self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return True
trie=Trie()
trie.insert("apple")
trie.insert("banana")
print(trie.search("apple"))
print(trie.prefix("bant"))                                          