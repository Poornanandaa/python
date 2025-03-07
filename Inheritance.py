class Parent(object):
    def __init__(self, eyes, hair):
        self.eyes = eyes
        self.hair = hair
    def display(self):
        print("My eyes are", self.eyes)
        print("My hair is", self.hair)
class child(Parent):
    def __init__(self, eyes, hair, short, athletic):
        self.short = short
        self.atletic = athletic        
        Parent.__init__(self, eyes, hair)
a = child("blue", "brown", "4 foot", "fast")
a.display()

        