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
    def delete(self,word):
        def _delete(node,word,depth):
            if depth==len(word):
                if not node.is_end:
                    return False
                node.is_end=False
                return len(node.children)==0
            char=word[depth]
            if char not in node.children:
                return False
            child_node=node.children[char]
            delete_child=_delete(child_node,word,depth+1)
            if delete_child:
                del node.children[char]
                return len(node.children)==0 and not node.is_end
            return False
        _delete(self.root,word,0)

trie=Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))
print(trie.prefix("app")) 
trie.delete("app")
print(trie.search("app"))      

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
    def count_word(self,node=None):
        if node is None:
            node=self.root
        count=0
        if node.is_end:
            count+=1
        for i in node.children.values():
            count+=self.count_word(i)
        return count
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
print(trie.count_word())    
print(trie.longest_common_prefix(arr))    