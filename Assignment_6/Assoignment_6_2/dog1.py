class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"My dog name is {self.name} and he {self.age} years old.")
    
    def get_info(self):
        print(f"My dog coat color is {self.coat_color}.")
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def display(self):
        print( f"My dog coat color is {self.coat_color}.")

    def info(self):
        print(f"My dog name is {self.name} and he {self.age} years old.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def display(self):
        print(f"My dog coat color is {self.coat_color}.")
    
    def info(self):
        print(f"My dog coat color is {self.coat_color}.")


c = JackRussellTerrier("jhonson",1.5,"pink")  
c.description()
c.get_info()  
b = Bulldog("sheru",2 ,"brown")
b.description()
b.get_info()
a = Dog("sweety" , 1 ,"black")
a.description()
a.get_info()


