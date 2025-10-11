# def count_vowels(s):
#     vowels="aeiou"
#     return sum( 1 for i in s if i in vowels)
# print(count_vowels("sneha"))  

# str1="sky is blue"
# print(" ".join(str1.split()[::-1]))

a=["aple","banana","grape"]
res=list(map(lambda x:x[::-1],a))
print(res)

def count(n):
    b=""
    for i in n:
        if str(i) not in b:
            b+=str(i)
    return [int(x) for x in b]
n=[1,1,2,3]    
print(count(n))    

# def rev(s):
#     return s[::-1]    
#     return s.upper()
#     return s[0].upper()+s[1:-1]+s[-1].upper()
#     return s.replace('a','w')
#     return s.split()
# print(rev("sneha is a cute"))  

s="hello"
swapped=s[-1]+s[1:-1]+s[0] if len(s)>1 else s
print(swapped)

cap_first = lambda s: s[0].upper() + s[1:] if s else s
print(cap_first("hello"))  

li=["string","is","immuntable"]
mi=min(li,key=len)
index=li.index(mi)
li.pop(index)
print(li)
                    

# a=[1,2,3,4,"string"]
# a.append(7)
# a.extend([8,7])
# a.insert(0,0)
# a.sort(reverse=True)
# print(a)
# print(set(a))
# b=[x for x in a if isinstance(x,str)]
# print(b)

# l=[i**2 for i in range(1,6)]
# print(l)

li=[1,2,3,4]
output=list(map(lambda x:x**3,li))
print(output)
print(list(filter(lambda x:x%2==0,li)))

# even = [i for i in range(10) if i %2 ==0 ]
# print(even)

nums=[1,2,3,4,4,2,5]
duplicates = [x for x in set(nums) if nums.count(x)>1]
print(duplicates)

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = {6, 7}
my_set.update(my_list) 
my_set = my_set | set(my_list) or my_set.update(set(my_list))
print(my_set)

def is_as(list1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            return False
    return True
list1=[1,2,3,4,5]    
print(is_as(list1))

d={'a':1,'b':2,'c':3,'d':4}
keys=[]
for key,value in d.items():
    if value%2!=0:
        keys.append(key)
for key in keys:
    del d[key]
print(d)    
        

d={"name":"sneha","age":23}
# b={"a":1,"b":2}
# d["grade"]="A"
# d["age"]=12
# d.update({"place":"chennai","blood":"AB+"})
# print(d.keys())
del d["age"]
# d.pop("age")
print(d)
# merged={**d,**b}
# merged=d | b
# d.update(b)
# print(merged)
for key,value in d.items():
    print(f"{key}-->{value}")

d1={"a":1,"b":2}
d2={"c":3,"b":8}

merge={}
for k,v in d1.items():
    merge[k]=v
for k,v in d2.items():
     if k in merge:
         merge[k]+=v
     else:
         merge[k]=v
print(merge)             

# squares = {z:z**2 for z in range(1,10)} 
# print(squares)   

sq={i:i**3 for i in range(10) if i%2!=0}
print(sq)

# d={"a":1,"b":2,"c":3,"d":4}
# d={k:v for k,v in d.items() if v%2==0}
# print(d)

# item=list(d.items())
# half=len(item)//2
# d1=dict(item[:half])
# d2=dict(item[half:])
# print(d1,d2)


# dic={1:"one","two":"two","three":"age"}
# output={k:v for k,v in dic.items() if isinstance(k,str)}
# print(output)

a={"a":1,"b":"sbs","c":"r","d":2.3}
keys=[]
for key,value in a.items():
    if not isinstance(value,str):
        keys.append(key)
for key in keys:
    del a[key]
print(a)    

def filter_dict(dic,key):
    return [d for d in dic if key not in d]
dic=[{"a":1,"b":2},{"c":3},{"a":4,"d":5}]
print(filter_dict(dic,"a"))

dicts=[{'a':1,'b':2},{'a':3,'c':4},{'a':5,'d':6}]
print(tuple(d['a'] for d in dicts))

# users=[
#     {"id":1,"name":"Alice","age":13},
#     {"id":2,"name":"Bob","age":23},
#     {"id":3,"name":"Charlie","age":33},
# ]
# names=[user["name"] for user in users]
# print(names)
# ages=[user for user in users if user["age"]>25]
# print(ages)
# for user in users:
#     user["email"]=user["name"].lower()+"@gmail.com"
# print(users)    

students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "grade": "A",
        "courses": {"math": 95, "science": 90, "history": 85}
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 21,
        "grade": "B",
        "courses": {"math": 85, "science": 80, "history": 88}
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 19,
        "grade": "B",
        "courses": {"math": 88, "science": 82, "history": 80}
    }
]
subjects=[list(s["courses"].keys()) for s in students]
print(subjects)
grade=[s["name"] for s in students if s["grade"]=="A"]
print(grade)
mark=[s["name"] for s in students if s["courses"]["math"]>90]
print(mark)
avg=sum( s["courses"]["history"] for s in students)/len(students)
print(avg)
sort=sorted(students,key=lambda s:s["age"])
print(sort)
print(sorted(list(key=lambda x:x['age'],reverse=True)))

# d={"a":[1,2,3],"b":[4,5,6],"c":[10,0,0]}
# output=max(d,key=d.get)
# del d[output]
# print(d)

# a={"a":[1,2,3],"b":[4,5,6],"c":[7,8,9],"d":[10,11,12]}
# output=sorted(a,key=a.get)
# del a[output[-2]]
# print(a)

def all_key(d):
    if not d:
        return True
    first_key=type(next(iter(d)))
    for key in d:
        if type(key) != first_key:
            return False
    return True
dict1={"hello":12,"game":"bobjy",90:90}
print(all_key(dict1))

l=["abc","a","abcd"]
l.pop(l.index(min(l,key=len)))
print(l)

d={"a":[7,3,3],"b":[6,6,5],"c":[1,2,3]}
a=max(d,key=lambda k:len(set(d[k])))
print(a)

d={"a":"apple","b":"ball","c":"call"}
s=max(d,key=lambda k:len(d[k]))
del d[s]
print(d)

k=sorted(d.items(),key=lambda x:len(x[1]))
lk,lv=k[-1]
del d[lk]
print(d)

s="my name is s sneha"
d={}
result=""
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    if d[i]==2:
        result+=i.upper()
    else:
        result+=i
print(result)   

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'])
print(sorted_students)

d = {
  "a": {"score": 80, "age": 20},
  "b": {"score": 90, "age": 22},
  "c": {"score": 75, "age": 21}
}
max_score=float('-inf')
max_key=""
for k,v in d.items():
    if v["score"]>max_score:
        max_score=v["score"]
        max_key=k
print(max_key)   

maxi=max(d,key=lambda x:d[x]["score"])
print(maxi)

# try:
#     x=10/0
#     b=10/2
# except  ZeroDivisionError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")            

# for i in range(5):
#    if  i == 5:
#       break
# else:
#    print("loop completed")   

# import copy
# a=[[1,2],3]

# shallow=copy.copy(a)
# deep=copy.deepcopy(a)
# a[0][0]=9

# print(a)
# print(deep)
# print(shallow)

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# def prime(arr):
#     return [i for i in arr if is_prime(i)]  

# arr=[4,7,10,11]
# print(prime(arr))  

# def sum(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i
#     return total
# print(sum(10))    

# def move_zeros_to_end(nums):
#     j = 0  
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[j] = nums[j], nums[i] 
#             j += 1
#     return nums
# nums = [0, 1, 0, 3, 12]
# print(move_zeros_to_end(nums)) 

# def move_zeros_to_front(nums):
#     j=len(nums)-1
#     for i in range(len(nums)-1,-1,-1):
#         if nums[i]!=0:
#             nums[i],nums[j]=nums[j],nums[i]
#             j-=1
#     return nums
# nums=[0,1,0,3,12]
# print(move_zeros_to_front(nums))
          

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("j",end=" ")
#     print()    

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for k in range(i+1):
#         print(" ",end=" ")    
#     print()    

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")    
#     print()    

# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):  
#         print(j,end=" ")
#     print()     

# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()    

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()  

def star_pyr(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"*"*(2*i+1))
star_pyr(5)       

for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# n=5
# for i in range(n-1,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()    

# n=5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()  


nums =[10,20,30,40,50,60]
mid = (len(nums)-1)//2
nums.pop(mid)
print(nums)

def key_same(d):
    return len({type(k) for k in d.keys()}) == 1
print(key_same({"a":1,"b":2}))    

from datetime import datetime

now = datetime.now()
print("Current datetime:", now)
print("Current time only:", now.strftime("%H:%M:%S"))
print("Current date only:", now.strftime("%Y-%m-%d"))


my_list = ["short", "medium", "very"]
max_len = max(len(s) for s in my_list)
for item in my_list:
    print(f"{item:>{max_len}}")

def first_last_key(d):
    if not d:
        return None
    keys=list(d.keys())
    return (keys[0],keys[-1])
d={"name":"sneha","age":89,"place":"paris"}
print(first_last_key(d))  

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

li=[1,-2,3,"hello",3.5,-2]
total=0
for i in li:
    if isinstance(i,(int,float)) and i>0:
        total+=i
print(total)    

s="geekss"
res=[]
for i in set(s):
    if s.count(i)>1:
        res.append(i)
print(res)        

def second(arr):
    if len(arr)<2:
        return None
    lar=float('-inf')
    slar=float(['-inf'])
    for i in arr:
        if i > lar:
            slar=lar
            lar=i
        elif i > slar and i!=lar:
            slar=i
    if slar == float('-inf'):    
        return None
    return slar
arr=[1,2,3,4,5]
print(second(arr))       

def rev(lst):
    left=0
    right=len(lst)-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
    return lst
lst=[1,2,3,4]
print(rev(lst))

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
        