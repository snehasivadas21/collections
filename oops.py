# class Bank:
#     def __init__(self,account_holder,balance=0):
#         self.account_holder=account_holder
#         self.balance=balance
#     def deposite(self,amount):
#         if amount > 0 :
#             self.balance+=amount
#             return f"{amount}---{self.balance}"
#         return "Invalid"
#     def withdraw(self,amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             return f"{amount}---{self.balance}"
#         return "Invalid"
#     def check_Bal(self):
#         return f"{self.account_holder}-{self.balance}"

# acc=Bank("sneha",1000)
# print(acc.deposite(50))
# print(acc.withdraw(30))
# print(acc.check_Bal())   
  
class Parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"{self.name}")
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def display(self):
        super().display()
        print(f"{self.name}---{self.age}")
obj=Child("sneha",45)
obj.display()

class Person:
    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin 

    def get_pin(self):
        return self.__pin
class Child(Person):
    def __init__(self, name, pin, age):
        super().__init__(name, pin)
        self.age = age

    def display(self):
        print(self.name, self.age)

ch = Child("hello", 1234, 34)
ch.display()
print(ch.get_pin())  

        
# class Animal:
#     def speak(self):
#         return "sound"
# class Dog(Animal): # dog inherit from animal and override speak
#     def speak(self):
#         return "woof"
# dog=Dog()  
# print(dog.speak()) 

class Bank:
    def __init__(self,name,dept,salary):
        self.name=name
        self._dept=dept
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
b=Bank("sneha","HR",50000)
print(b.name)    
print(b._dept)    
# print(b.__salary)
print(b.get_salary())  #getter
print(b._Bank__salary) #name mangling
b.set_salary(55000) #setter

class Emp:
    def __init__(self,salary):
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,amount):
        if amount>0:
            self.__salary=amount
e=Emp(60)
print(e.salary)
e.salary=70
print(e.salary)

class Human:
    def __init__(self,age):
        self.__age=age
    @property    
    def age(self):
        return self.__age
class Robot(Human):
    def __init__(self,name,id,age):
        super().__init__(age)
        self.name=name
        self.id=id
    @property
    def get(self):
        return self.name,self.age
        
r=Robot("a",1,30)
print(r.name)
print(r.age)
print(r.get)

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.lenght=length
#         self.breadth=breadth
#     def area(self):
#         return self.lenght * self.breadth
# r=Rectangle(5,4)
# print(r.area()) 

class Student:
    count = 0  
    def __init__(self, name):
        self.name = name
        Student.count += 1  
s1 = Student("Alice")
s2 = Student("Bob")
print("Number of instances:", Student.count)
class Human:
    count=0
    @classmethod
    def class_method(cls):
        cls.count+=1
Human.class_method()
Human.class_method()
print(Human.count)
class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def grade(self):
        avg=sum(self.mark.values())/len(self.mark)
        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=60:
            return "C"
        else:
            return "D"
s=Student("Sneha",{"a":90,"c":80})
print(s.grade())

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 * self.radius ** 2  
# c=Circle(5)
# print(c.area())

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self,base,bonus):
        self.base=base
        self.bonus=bonus
    def calculate_salary(self):
        return self.base+self.bonus
class Developer(Employee):
    def __init__(self,base,hours,rate):
        self.base=base
        self.hours=hours
        self.rate=rate
    def calculate_salary(self):
        return self.base+(self.hours*self.rate)
m=Manager(5000,1000)
d=Developer(4000,20,500)
print(m.calculate_salary())
print(d.calculate_salary())

# class Audio:
#     def play(self):
#         print("audio")
# class Video:
#     def play(slef):
#         print("video")
# def play_media(media):
#     media.play()
# audio=Audio()
# video=Video()
# play_media(audio)
# play_media(video)                

import random
# random_num=lambda : random.randint(1,10)
# print(random_num())

# def rand_not_five():
#     random_num = random.randint(1,10)
#     while random_num==5:
#         random_num = random.randint(1,10)
#     return random_num
# print(rand_not_five())    
 
import math
square=lambda x:(math.sqrt(x))**2
print(square(5))

from datetime import datetime,timedelta,date

print((datetime.now()-timedelta(days=5)).strftime('%Y-%m-%d'))

now = datetime.now()
print("Current datetime:", now)
print("Current time only:", now.strftime("%H:%M:%S"))
print("Current date only:", now.strftime("%Y-%m-%d"))
print(datetime.now().time())
print(datetime.now().date())
print(datetime.today().strftime("%Y"))
print(datetime.today().strftime("%B"))
print(datetime.today().strftime("%W"))
print(datetime.today().strftime("%j"))
print(datetime.today().strftime("%d"))
print(datetime.today().strftime("%A"))

today=date.today()
new_year=date(today.year+1,1,1)
print((new_year-today).days)
 
# def count(n):
#     for i in range(1,n+1):
#         yield i
# for z in count(5):
#     print(z)      

# def squares(n):
#     for i in range(n):
#         yield i**2
# for i in squares(5):
#     print(i) 

def even_numbers():
    i = 2
    while True:
        yield i
        i += 2
evens = even_numbers()
print(next(evens))  # 2
print(next(evens))  # 4
print(next(evens))  # 6

def fib(n):
    a=0
    b=1
    for _ in range(n):
        yield a
        a,b=b,a+b
for i in fib(10):
    print(i,end=" ")
print()    

def prime_generator():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True   
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1
gen = prime_generator()
for _ in range(5):
    print(next(gen))  

# def read_file(path):
#     with open(path,'r') as file:
#         for line in file:
#             yield line
# for line in read_file("bigdata.txt"):
#     print(line.strip())        

# a=[1,2,3]
# b=iter(a)
# print(next(b))  

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
    
# class Person:
#     sleeptime =8
#     @staticmethod
#     def static_method():
#         print(Person.sleeptime)
#     @classmethod
#     def class_method(cls):
#         print(cls.sleeptime)
# Person.static_method()
# Person.class_method()     

# def decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
# @decorator
# def hello():
#     print("hello world")
# hello()        

def uppercase_decorator(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        if isinstance(result,str):
            return result.upper()
        return result
    return wrapper    
@uppercase_decorator
def greet():
    return "hello world"
print(greet())   

def divide_safe(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    return wrapper
@divide_safe
def divide(a, b):
    return a / b
print(divide(10, 2))  
print(divide(5, 0))   

def decorator(func):
    def wrapper(*args,**kwargs):
        print("access")
        func(*args,**kwargs)
    return wrapper
@decorator
def add(a,b):
    print(a+b)
add(5,4)    
      
# import time
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f"{end-start:.4f}->{func.__name__}")
#         return result
#     return wrapper
# @decorator
# def reverse(s):
#     time.sleep(5)
#     output=[]
#     s=s.split()
#     for i in s:
#         output.append(i[::-1])
#     return " ".join(output)
# print(reverse("hello leetcode"))    

# import os
# with open("text.txt","w") as f:
#     f.write("hello")
# with open("text.txt","r") as f:
#     print(f.read())  
# os.remove("text.txt")  

class A:
    def hello(self):
        print("A")
class B(A):
    def hai(self):
        print("B")
class C(B):
    pass
obj=C()
obj.hello()
obj.hai()  

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)
    def __repr__(self):
        return f"{self.x},{self.y}"
v1=Vector(2,3)
v2=Vector(4,1)
print(v1+v2)
print(v1*3)
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
        print(f"{item}")
    def dequeue(self):
        if self.is_empty():
            print("empty")
            return None
        removed=self.items.pop(0)
        return removed
    def is_empty(self):
        return len(self.items)==0
    def display(self):
        print(self.items)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
q.dequeue()
