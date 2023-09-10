class Employee:
    company = "Camel"
    salary = 100
    location = 'Delhi'

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal
    #     self.salary = sal

    @classmethod                                        #This is decorator this is function
    def changeSalary(cls,sal):
        cls.salary = sal
    #classmethod is bound to the class not the object    


e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
