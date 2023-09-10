class Person:
    country ="India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    # def takeBreath(self):
    #         print("I am employeee so i am luckily breathing..")

class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
         print("I am programmer so I am breathing++...")

p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(p.country)
