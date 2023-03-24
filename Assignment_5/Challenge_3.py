class Student:

    def __init__(self):
        self.name = None  
        self.rollnumber = None

    def setName(self , name):
        self.name = name

    def getName(self):
        return self.name
    
    def setRollNumber(self , rollnumber):
        self.rollnumber = rollnumber

    def getRollNumber(self):
        return self.rollnumber
    
result = Student()
result.setName("Savita")
print(result.getName())
result.setRollNumber("101")
print(result.getRollNumber())