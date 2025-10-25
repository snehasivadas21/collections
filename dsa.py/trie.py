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

class Trienode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=Trienode()
    def insert(self,word):
        cur=self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=Trienode()
            cur=cur.children[i]
        cur.is_end=True
    def dfs(self,node,prefix,result): #collect all the node under that prefix
        if node.is_end:
            result.append(prefix)
        for char,child in node.children.items():
            self.dfs(child,prefix+char,result)
    def autocomplete(self,prefix): #find the prefix node
        cur=self.root
        for i in prefix:
            if i not in cur.children:
                return []
            cur=cur.children[i]
        result=[]
        self.dfs(cur,prefix,result)
        return result
t=Trie()
words=["goes","go","apple","app"]
for i in words:
    t.insert(i)
print(t.autocomplete("ap"))   

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
    def longest_common_prefix(self,strs):
        if not strs:
            return  ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        common_prefix=[]
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                common_prefix.append(first[i])
            else:
                break
        return "".join(common_prefix)
trie=Trie()
arr=["flower","flow","flat"]
for i in arr:
    trie.insert(i)
print(trie.longest_common_prefix(arr))    