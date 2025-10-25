# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"{self.name}")
# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def display(self):
#         super().display()
#         print(f"{self.age}")
# ch=Child("sneha",10)
# ch.display()

# a=[1,2,3,4]
# a.insert(3,0)
# print(a)
# sq=[i for i in a if i%2==0]
# print(sq)

# d={"name":"sneha","age":78}
# d["person"]="aa"
# print(d)

def remove_str(arr):
    i=0
    while i<len(arr):
        if isinstance(arr[i],str):
           arr.pop(i)
        else:
            i+=1
    return arr        
print(remove_str(["2",2,"3",3,"1",3,4,"8"]))           

def remove_str(arr):
    return [i for i in arr if not isinstance(i,str)]
print(remove_str(["3",3,"1",3,4,"8"]))           

students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "math": 95
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 21,
        "math": 85
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 19,
        "math": 88
    }
]
print(i["name"] for i in students if i["math"]>85)

d={'apple': 3, 'banana': 1, 'cherry': 2}
d1={'banana': 1, 'cherry': 2, 'apple': 3}

print(dict(sorted(d.items(),key=lambda x:x[1],reverse=True)))

def factorial(n):
    if n<=1:
        return n
    return n*factorial(n-1)
print(factorial(5))

def sum(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    return total
print(sum([1,2,3,4,5]))    

def bubble(arr):
    while True:
        a=True
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                a=False
        if a==True:
            break
arr=[22,1,34,2,1]
bubble(arr)
for i in arr:
    print(i,end=" ")   
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def delete_front(self):
        if not self.head:
            return None
        self.head=self.head.next
    def traverse(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ->")
            curr=curr.next
        print("None")
ll=Linkedlist()
arr=[1,2,3,4]
for i in arr:
    ll.insert_end(i)
ll.traverse()    
ll.delete_front()
ll.traverse()
                         