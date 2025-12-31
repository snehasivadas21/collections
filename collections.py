# def rev(s):
#     return s[::-1]    
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

s="geekss"
res=[]
for i in set(s):
    if s.count(i)>1:
        res.append(i)
print(res)

s="hello"
swapped=s[-1]+s[1:-1]+s[0] if len(s)>1 else s
print(swapped)

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

my_list = ["short", "medium", "very"]
max_len = max(len(s) for s in my_list)
for item in my_list:
    print(f"{item:>{max_len}}")

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

def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        permute(left + right, answer + ch)
permute("ABC")


