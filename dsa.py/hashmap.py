# def char_freq(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(char_freq("hello world")) 

# def non_repeating(s):
#     d={}
#     for i in s:
#         d[i]=d.get(i,0)+1
#     for i in reversed(s):
#         if d[i]==1:
#             return i    
# print(non_repeating("abbc")) 

def least(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    sorted_items = sorted(d.items(),key=lambda x:x[1])
    return [sorted_items[0][0],sorted_items[1][0]]

nums=[1,1,2,2,2,3,4,4,5]
print(least(nums))

a="programming"
d={}
for i in a:
    d[i]=d.get(i,0)+1
r=""    
for i in a:
    if d[i]==1:
        r+=i
print(r)        

def first_rep(a):
    d={}
    for i,v in enumerate(a):
        if v in d:
            return v
        d[v]=i
a=[1,2,3,3,4,4]
print(first_rep(a))

# def is_anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     count={}
#     for i in s1:
#         if i not in count:
#             count[i]=1
#         else:
#             count[i]+=1
#     for i in s2:
#         if i not in count:
#             return False
#         count[i]-=1
#     for i in count.values():
#         if i!=0:
#             return False
#     return True
# s1="triangle"
# s2="integral"
# print(is_anagram(s1,s2))

class Hash:
    def __init__(self,size=10):
        self.size=size
        self.table=[[] for _ in range(size)]
    def hash_func(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index=self.hash_func(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i]=(key,value)
                return 
        self.table[index].append((key,value))
    def get(self,key):
        index=self.hash_func(key)
        for k,v in self.table[index]:
            if k==key:
                return v
        return None
    def delete(self,key):
        index=self.hash_func(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                del self.table[index][i]
                return False
        return True
h=Hash()
h.insert("a",10)
h.insert("b",20)
print(h.get("b"))
print(h.table)
h.delete("a")
print(h.table)

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Hashtable:
    def __init__(self,size=10):
        self.size=size
        self.table=[None]*size
        
    def _hash(self,key):
        return hash(key)%self.size
        
    def insert(self,key,value):
        index=self._hash(key)
        head=self.table[index]
        curr=head
        while curr:
            if curr.key==key:
                curr.value=value
                return 
            curr=curr.next
        new_node=Node(key,value)
        new_node.next=head
        self.table[index]=new_node
    
    def get(self,key):
        index=self._hash(key)
        curr=self.table[index]
        while curr:
            if curr.key==key:
                return curr.value
            curr=curr.next
        return None
    
    def delete(self,key):
        index=self._hash(key)
        curr=self.table[index]
        prev=None
        while curr:
            if curr.key==key:
                if prev:
                    prev.next=curr.next
                else:
                    self.table[index]=curr.next
                    return True
            prev=curr
            curr=curr.next 
        return False            
    
    def display(self):
        for i in range(self.size):
            print(f"{i}",end="  ")
            curr=self.table[i]
            while curr:
                print(f"({curr.key}-{curr.value})",end="  ")
                curr=curr.next
            print("None")
            
h=Hashtable(5)
h.insert("a",50)
h.insert("b",60)
h.insert("c",30)
h.insert("d",20)
h.insert("e",40)
h.display()
h.get("d")

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = "DELETED" 

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        start_index = index
        
        while self.table[index] is not None and self.table[index] != self.DELETED:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return           
            index = (index + 1) % self.size       
            if index == start_index:
                raise Exception("Hash Table is full")       
        self.table[index] = (key, value)  
    
    def search(self, key):
        index = self._hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None  
    
    def delete(self, key):
        index = self._hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
            if index == start_index:
                break
        return False   

ht = HashTable(5)
ht.insert(1, "A")
ht.insert(6, "B")   
ht.insert(11, "C")  
print(ht.table)
ht.delete(6)
print(ht.search(11))       
        

