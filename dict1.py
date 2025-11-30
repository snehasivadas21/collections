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

d={'a':1,'b':2,'c':3,'d':4}
keys=[]
for key,value in d.items():
    if value%2!=0:
        keys.append(key)
for key in keys:
    del d[key]
print(d) 

def filter_dict(dic,key):
    return [d for d in dic if key not in d]
dic=[{"a":1,"b":2},{"c":3},{"a":4,"d":5}]
print(filter_dict(dic,"a"))

dicts=[{'a':1,'b':2},{'a':3,'c':4},{'a':5,'d':6}]
print(tuple(d['a'] for d in dicts))

numbers = [-3, -1, 0, 2, 5]
d={i:"positive" if i>0 else ("negative" if i<0 else "zero") for i in numbers}
print(d)

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

# d={"a":[1,2,3],"b":[4,5,6,7],"c":[10,0,0]}
# output=max(d,key=d.get)
# del d[output]
# print(d)

s=max(d,key=lambda k:len(d[k]))
del d[s]
print(d)

# a={"a":[1,2,3],"b":[4,5,6],"c":[7,8,9],"d":[10,11,12]}
# output=sorted(a,key=a.get)
# del a[output[-2]]
# print(a)

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

text = "Beautiful morning in the valley"
vowels="aeiouAeiou"
d={i: text.count(i) for i in vowels if i in text}
print(d)

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

d=[k for k,v in d.items() if v["score"]>85]
print(d)

data = {
    "a": {"marks": [10, 20, 30]},
    "b": {"marks": [5, 15]},
    "c": {"marks": [50, 10, 40]}
}

d={}
for k,v in data.items():
    d[k]=sum(v["marks"])
print(max(d,key=d.get))   

s=max(data,key=lambda x:sum(data[x]["marks"]))
print(s)

s={k:sum(v["marks"]) for k,v in data.items()}
print(s)

d=[k for k,v in data.items() if len(v["marks"])>1]
print(d)

d=sorted(data,key=lambda x:sum(data[x]["marks"]),reverse=True)[:2]
print(d)

dept_salaries = {
    "CSE": [50000, 60000, 70000],
    "ECE": [45000, 55000, 65000],
    "MECH": [40000, 42000, 43000]
}

max_avg=0
high_dept=""
for d,s in dept_salaries.items():
    total=0
    count=0
    for i in s:
        total+=i
        count+=1
    avg=total/count
    if avg>max_avg:
        max_avg=avg
        high_dept=d
del dept_salaries[high_dept]
print(high_dept)
print(dept_salaries)

def first_last_key(d):
    if not d:
        return None
    keys=list(d.keys())
    return (keys[0],keys[-1])
d={"name":"sneha","age":89,"place":"paris"}
print(first_last_key(d)) 

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

a={'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
unique={}
seen=set()
for k,v in a.items():
    if v not in seen:
        unique[k]=v
        seen.add(v)
print(unique)        

words = ['apple', 'ant', 'banana', 'bat', 'cat', 'car']
d={}
for i in words:
    first=i[0].lower()
    if first not in d:
        d[first]=[]
    d[first].append(i)
print(d)  
print({i:words.count(i) for i in words}) 

data = {"a": 1, "b": 2, "c": 1, "d": 3}
d={}
for k,v in data.items():
    if v not in d:
        d[v]=[]
    d[v].append(k)
print(d)  

