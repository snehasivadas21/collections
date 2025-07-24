class Animal:
    def speak(self):
        return "sound"
class Dog(Animal): # dog inherit from animal and override speak
    def speak(self):
        return "woof"
dog=Dog()  
print(dog.speak())  

import random
random_num=lambda : random.randint(1,10)
print(random_num())
    