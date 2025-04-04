class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Meow")   
    def info(self):
        print(f"I am a cat, My name is {self.name}, My info is {self.age}")
class Dog:
    def __init__(self, name, info):
        self.name = name
        self.age = info 
    def make_sound(self):
        print("Bark")   
    def info(self):
        print(f"I am a dog, My name is {self.name}, My info is {self.age}") 
cat1 =  Cat("Jerry", 5)  
dog1 =  Dog("Poodle", 6)     
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()       

