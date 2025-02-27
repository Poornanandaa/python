class Robot:
    def __init__(self, name):
        self.name = name

    def some_method(self):
        print("Hello, my name is{self.name}. I am a robot.")
robot1=Robot("Tom")      
robot2=Robot("Jerry")  
print("robot1.name is Tom")
print("robot2.name is Jerry")