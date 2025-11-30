# a=[1,2,3,4,"string"]
# a.append(7)
# a.extend([8,7])
# a.insert(0,0)
# a.sort(reverse=True)
# print(a)
# print(set(a))
# b=[x for x in a if isinstance(x,str)]
# print(b)

l=[i**2 for i in range(1,6)]
print(l)

list1 = [1, 2]
list2 = ['a', 'b', 'c']
l=[(x,y) for x in list1 for y in list2]
print(l)

even = [i for i in range(10) if i %2 ==0 ]
print(even)

ds = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie", "David"]
l_d = [{"id":i,"name":n} for i,n in zip(ds,names)]
print(l_d)

a=[1,2,3,4]
b=[1,2,3,4]
c=[i*x for i,x in zip(a,b)]
print(c)

a=[1,2,3,4,5,6]
n=3
result=[a[i:i+n] for i in range(0,len(a),n)]
print(result)

l1 = [1, 2, 2, 3, 4]
l2 = [3, 4, 4, 5, 6]
print(list(set(l1) & (set(l2))))
print(list(set(l1) | (set(l2))))
print(list(set(l1) ^ (set(l2))))

x = 2
y = 3
a=lambda x,y:0.5*x*y
a=a(x,y)
print(a)

li=[1,2,3,4]
output=list(map(lambda x:x**3,li))
print(output)
print(list(filter(lambda x:x%2==0,li)))

numbers = [10, 15, 25, 33, 45, 52, 65]
b=list(filter(lambda x:x%10==5,numbers))
print(b)

data = [(1, 3), (2, 1), (4, 2), (3, 5)]
b=sorted(data,key=lambda x:x[-1])
print(b)

a=["aple","banana","grape"]
res=list(map(lambda x:x[::-1],a))
print(res)

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'])
print(sorted_students)

s=sorted(students,key=lambda x:len(x["name"]))
print(s)

def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15]
p=list(filter(lambda x:prime(x),numbers))
print(p)

nums=[1,2,3,4,4,2,5]
duplicates = [x for x in set(nums) if nums.count(x)>1]
print(duplicates)

d=[2, 2, 1, 2, 3, 2, 2]
count={}
for i in d:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
print(max(count,key=count.get))            

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
f=[matrix[i][i] for i in range(len(matrix))]
print(f)
s=[matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
print(s)

def merge(a,b):
    i=len(a)-1
    j=0
    while i>=0 and j<len(b):
        if a[i]<b[j]:
            i-=1
        else:
            a[i],b[j]=b[j],a[i]
            i-=1
            j+=1
    a.sort()
    b.sort()
a=[1, 4, 7, 8, 10]
b=[2, 3, 9]
merge(a,b)
print(a)
print(b)

a=[100, 4, 200, 1, 3, 2]
num_set=set(a)
longest=0
for i in num_set:
    if i-1 not in num_set:
        curr=i
        length=1
        while curr+1 in num_set:
            curr+=1
            length+=1
    longest=max(longest,length)
print(longest)  

def bineary(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=x<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<x<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1            
arr=[6, 7, 8, 1, 2, 3, 4, 5]
x=3
print(bineary(arr,x))

a=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
msum=float('-inf')
s=0
for i in a:
    s+=i
    msum=max(msum,s)
    if s<0:
        s=0
print(msum)    
   
a=[[1,2],[3,4]]
b=[j for i in a for j in i]
print(b)

def flattend(a):
    flat=[]
    for i in a:
        if isinstance(i,list):
            flat.extend(flattend(i))
        else:
            flat.append(i)
    return flat        
a=[1,2,[3,4,[4,5,6,[7]]]]
print(flattend(a))

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

l=["abc","a","abcd"]
l.pop(l.index(min(l,key=len)))
print(l)

def linear_search(arr,x):
    for index,item in enumerate(arr):
        if item==x:
            return index
arr=[22,12,32,52,42]
x=52
print(linear_search(arr,x))

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

def missing(arr):
    n=len(arr)+1
    hash=[0]*(n+1)
    for i in range(n-1):
        hash[arr[i]]+=1
    for i in range(1,n+1):
        if hash[i]==0:
            return i
    return -1
arr=[3,2,1,4,6]   
print(missing(arr))

li=[1,-2,3,"hello",3.5,-2]
total=0
for i in li:
    if isinstance(i,(int,float)) and i>0:
        total+=i
print(total)   

my_list = [1, 2.5, 3, "hello", 4.0, 5, True, 6.7]
result=[]
for i in my_list:
    if isinstance(i,int) and not isinstance(i,bool):
        result.append(str(i))
print(result)        

nums =[10,20,30,40,50,60]
mid = (len(nums)-1)//2
nums.pop(mid)
print(nums)

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