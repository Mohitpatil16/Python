#Class Attributes:
#The attribute that are directly link to the class is called the class attribute.
class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajani = Employee()
harry.salary = 300
rajani.salary = 400
print(harry.company)
print(rajani.company)
Employee.company="Youtube"
print(harry.company)
print(rajani.company)

print(harry.salary)
print(rajani.salary)