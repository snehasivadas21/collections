# def rev(s):
#     return s[::-1]   
#     return s==s[::-1] 
#     return s.upper()
#     return s[0].upper()+s[1:-1]+s[-1].upper()
#     return s.replace('a','w')
#     return s.split()
# print(rev("sneha is a cute"))  

sentence = "An elephant is under an old oak tree"
vowels="aeiouAEIOU"
s=[i for i in sentence.split() if i[0] in vowels]
print(s)

# def count_vowels(s):
#     vowels="aeiou"
#     return sum( 1 for i in s if i in vowels)
# print(count_vowels("sneha"))

s="interview preparation helps you improve"
word=s.split()
vowels="aeiou"
m=max(word,key=lambda x:sum(1 for i in x if i in vowels))
c=["removed" if i==m else i for i in word]
print(" ".join(c))  

a="hello world"
vowels="aeiou"
result=[i for i in a if i not in vowels]
print("".join(result))
        
# str1="sky is blue"
# print(" ".join(str1.split()[::-1]))
# print(" ".join(i[::-1] for i in str1.split()))

def rev(sl):
    s=sl.split()
    l=0
    r=len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return " ".join(s)    
sl="sky is blue"
print(rev(sl))

def rev(s):
    r=s.split()
    output=[]
    for i in r:
        output.append(i[::-1])
    return " ".join(output)    
s="hello world"
print(rev(s))

def merge_rev(r):
    if len(r)<=1:
        return r
    mid=len(r)//2
    left=merge_rev(r[:mid])
    right=merge_rev(r[mid:])
    return right+left

r="hello"
l_r=list(r)
print("".join(merge_rev(l_r)))
        

def rev_vowel(s):
    vowels="aeiou"
    slist=list(s)
    l=0
    r=len(slist)-1
    while l<r:
        while l<r and slist[l] not in vowels:
            l+=1
        while l<r and slist[r] not in vowels:
            r-=1
        if l<r:
            slist[l],slist[r]=slist[r],slist[l]
            l+=1
            r-=1
    return "".join(slist)        
s="hello"        
print(rev_vowel(s))        

def count(n):
    b=""
    for i in n:
        if str(i) not in b:
            b+=str(i)
    return [int(x) for x in b]
n=[1,1,2,3]    
print(count(n)) 

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

def second_long(s):
    words=list(set(s.split()))
    words.sort(key=len,reverse=True)
    return words[1] if len(words)>=2 else None

s="Python is powerful and easy to learn"
print(second_long(s))

def sort_by_freq(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    sorted_items=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return "".join(i*count for i,count in sorted_items)
s="mississippi"    
print(sort_by_freq(s))

def upper_case(s,n):
    s=s.split()
    r=""
    for i in s:
        m=""
        for j in range(len(i)):
            if j==n:
                m+=i[j].upper()
            else:
                m+=i[j]
        r+=m+" "
    return r    
s="my name is sneha"
n=1
print(upper_case(s,n))

s="geekss"
res=[]
for i in set(s):
    if s.count(i)>1:
        res.append(i)
print(res)

s="hello"
swap_ends = lambda s: s[-1] + s[1:-1] + s[0] if len(s) > 1 else s
print(swap_ends(s))

def rotate(s,k):
    n=len(s)
    k=k%n
    return s[n-k:]+s[:n-k]
s="abcdef"
k=2
print(rotate(s,k))

li=["string","is","immuntable"]
mi=min(li,key=len)
index=li.index(mi)
li.pop(index)
print(li) 

def example(*args):
    if not args or all(arg is None for arg in args):
        raise ValueError("must not be None")
    return "success"
print(example("2",None))   

def example(**kwargs):
    if "err" in kwargs:
        raise ValueError("problem")
    print("success")
example(data="test")    
example(err="err")    

def all_same(*args):
    if not args:
        return True
    first=args[0]
    for arg in args:
        if arg!=first:
            return False
    return True
print(all_same("a","3",1))
print(all_same(1,1,1))

l="aaabbcdddd"
result=""
count=1
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        count+=1
    else:
        result+=l[i]+str(count)
        count=1
result+=l[-1]+str(count)        
print(result)

s="a5b4c3"
result=""
for i in range(0,len(s),2):
    char=s[i]
    count=int(s[i+1])
    result+=char*count
print(result) 

a="apple"
result=[]
for i in range(len(a)):
    result.append(a[i]*(i+1))
print("".join(result))    

a="aaabbccccd"
l=1
ml=1
r=a[0]
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        l+=1
    else:
        l=1
    if l>ml:
        ml=l
        r=a[i]
print(r*ml) 

def lar_sub(s):
    vowels="aeiou"
    max_sub=""
    curr=""
    for i in s:
        if i not in vowels:
            curr+=i
        else:
            if len(curr)>len(max_sub):
                max_sub=curr
            curr=""
    if len(curr)>len(max_sub):
        max_sub=curr
    return max_sub
s="strength"
print(lar_sub(s))

def permutations(s):
    if len(s) <= 1:
        return [s]   
    result = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        for p in permutations(remaining):
            result.append(char + p)
    return result
print(permutations("abc"))


