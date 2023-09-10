class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totSalary = 6000
    @property                                       #it is function but act as property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter                             #this is the property decorator
    def totalSalary(self,val):
        self.salarybonus = val-self.salary

e = Employee()
print(e.totalSalary)
print(e.salary)
e.totalSalary = 5800
print(e.salarybonus)