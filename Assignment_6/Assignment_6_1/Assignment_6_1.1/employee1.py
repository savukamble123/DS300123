import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read employee information from JSON file
with open("employee.json") as f:
    data = json.load(f)

employees = []
for emp in data:
    employees.append(Employee(emp["Name"], emp["DOB"], emp["Height"], emp["City"], emp["State"]))

for emp in employees:
    print(emp.__dict__)


