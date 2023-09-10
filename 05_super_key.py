class Person:
    country=  "India"
    def __init__(self):
        print("Initializing person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
            super().takeBreath()
            print("I am employeee so i am luckily breathing..")

class Programmer(Employee):
    company="Fiverr"

    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am programmer so I am breathing++...")

# p = Person()
# p.takeBreath()
# print(p.company)   #This throws the errror

# e = Employee()
# e.takeBreath()
# print(e.company)

pr = Programmer()
# pr.takeBreath()
# print(pr.company)
# print(p.country)
