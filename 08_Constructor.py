class Employee:
    company = "Google"
    
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")


    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    def getsalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def Greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9 Am in the morning")

# harry = Employee() --> This throws an error
harry = Employee ("Harry",100,"youtube")
harry.getDetails()