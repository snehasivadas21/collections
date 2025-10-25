# def non_repeating(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     for i in reversed(s):
#         if d[i]==1:
#             return i    
# print(non_repeating("abbc")) 

def first_rep(a):
    d={}
    for i,v in enumerate(a):
        if v in d:
            return v
        d[v]=i
a=[1,2,3,3,4,4]
print(first_rep(a))

# def char_freq(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(char_freq("hello world")) 

def remove(s):
    seen=set()
    result=[]
    for i in s:
        if i  not in seen:
            seen.add(i)
            result.append(i)
    return "".join(result)
s="geeksforgeeks"
print(remove(s))

def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count={}
    for i in s1:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    for i in s2:
        if i not in count:
            return False
        count[i]-=1
    for i in count.values():
        if i!=0:
            return False
    return True
s1="triangle"
s2="integral"
print(is_anagram(s1,s2))

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
