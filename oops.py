class Bank:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def deposite(self,amount):
        if amount > 0 :
            self.balance+=amount
            return f"{amount}---{self.balance}"
        return "Invalid"
    def withdraw(self,amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            return f"{amount}---{self.balance}"
        return "Invalid"
    def check_Bal(self):
        return f"{self.account_holder}-{self.balance}"

acc=Bank("sneha",1000)
print(acc.deposite(50))
print(acc.withdraw(30))
print(acc.check_Bal())        


# class Animal:
#     def speak(self):
#         return "sound"
# class Dog(Animal): # dog inherit from animal and override speak
#     def speak(self):
#         return "woof"
# dog=Dog()  
# print(dog.speak()) 

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.lenght=length
#         self.breadth=breadth
#     def area(self):
#         return self.lenght * self.breadth
# r=Rectangle(5,4)
# print(r.area())        


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

def rand_not_five():
    random_num = random.randint(1,10)
    while random_num==5:
        random_num = random.randint(1,10)
    return random_num
print(rand_not_five())    
 
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

def decorator(func):
    def wrapper(*args):
        print(f"{func.__name__}")
        return func(*args)
    return  wrapper
@decorator
def add(a,b):
   return a+b
print(add(5,6))   

import os
with open("text.txt","w") as f:
    f.write("hello")
with open("text.txt","r") as f:
    print(f.read())  
os.remove("text.txt")    