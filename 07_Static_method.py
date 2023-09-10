class Employee:
    company = "Google"
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def Greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9 Am in the morning")

harry = Employee() 
harry.salary= 100000
harry.getSalary("Thanks!") #Employee.getSalary(harry)
harry.Greet() #Employee.greet()
harry.time()