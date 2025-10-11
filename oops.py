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
        print(f"{self.age}")
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
b=Bank("sneha","HR",50000)
print(b.name)    
print(b._dept)    
# print(b.__salary)
print(b.get_salary())  #getter
print(b._Bank__salary) #name mangling

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


# a=[1,2,3]
# b=iter(a)
# print(next(b))         
    
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

# def decorator(func):
#     def wrapper(*args):
#         print(f"{func.__name__}")
#         return func(*args)
#     return  wrapper
# @decorator
# def add(a,b):
#    return a+b
# print(add(5,6))   

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
class B:
    def hai(self):
        print("B")
class C(A,B):
    pass
obj=C()
obj.hello()
obj.hai()  