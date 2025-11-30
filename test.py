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

# def remove_str(arr):
#     i=0
#     while i<len(arr):
#         if isinstance(arr[i],str):
#            arr.pop(i)
#         else:
#             i+=1
#     return arr        
# print(remove_str(["2",2,"3",3,"1",3,4,"8"]))           

# def remove_str(arr):
#     return [i for i in arr if not isinstance(i,str)]
# print(remove_str(["3",3,"1",3,4,"8"]))           

# students = [
#     {
#         "id": 1,
#         "name": "Alice",
#         "age": 20,
#         "math": 95
#     },
#     {
#         "id": 2,
#         "name": "Bob",
#         "age": 21,
#         "math": 85
#     },
#     {
#         "id": 3,
#         "name": "Charlie",
#         "age": 19,
#         "math": 88
#     }
# ]
# print(i["name"] for i in students if i["math"]>85)

# d={'apple': 3, 'banana': 1, 'cherry': 2}
# d1={'banana': 1, 'cherry': 2, 'apple': 3}

# print(dict(sorted(d.items(),key=lambda x:x[1],reverse=True)))
# print(dict(sorted(d.items(),key=lambda x:x[0][0])))

# def factorial(n):
#     if n<=1:
#         return n
#     return n*factorial(n-1)
# print(factorial(5))

# def sum(arr):
#     total=0
#     for i in range(len(arr)):
#         total+=arr[i]
#     return total
# print(sum([1,2,3,4,5]))   

# a=[(1,2,3),(2,3,4),(3,4,5)]
# d={}
# for i in range(len(a)):
#     if a[i] not in d:
#         d[i]=a[i]
# print(d)        

# def even(n):
#     for i in range(n-1,-1,-1):
#         if i%2==0:
#             yield i
# for i in even(10):
#     print(i)

# def bubble(arr):
#     while True:
#         a=True
#         for i in range(len(arr)-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#                 a=False
#         if a==True:
#             break
# arr=[22,1,34,2,1]
# bubble(arr)
# for i in arr:
#     print(i,end=" ")     
    
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Queue:
#     def __init__(self):
#         self.head=None
#     def enqueue(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#             return 
#         curr=self.head
#         while curr.next:
#             curr=curr.next
#         curr.next=new_node
#     def dequeue(self):
#         if not self.head:
#             return None
#         self.head=self.head.next
#     def traverse(self):
#         curr=self.head
#         while curr:
#             print(curr.data,end=" ->")
#             curr=curr.next
#         print("None")
# ll=Queue()
# arr=[1,2,3,4]
# for i in arr:
#     ll.enqueue(i)
# ll.traverse()    
# ll.dequeue()
# ll.traverse()

# def sum_digit(n):
#     if int(n)==0:
#         return 0
#     return (int(n)%10)+sum_digit(int(n)//10)
# n="1234"
# print(sum_digit(n))

# class Bank:
#     def __init__(self,name,pin):
#         self.name=name
#         self.__pin=pin
#     @property
#     def pin(self):
#         return self.__pin
#     @pin.setter
#     def pin(self,number):
#         if number>0:
#             self.__pin=number
# b=Bank("sneha",1234)
# print(b.name,b.pin)
# b.pin=4321
# print(b.pin)

def copy_file():
    with open("input.txt","r") as file:
        data=file.read()
    with open("output.txt","w") as file:
        file.write(data)
copy_file()  

from datetime import datetime

today=datetime.today()
last_day=datetime(today.year,12,31)
diff=last_day-today
print(diff.days)
