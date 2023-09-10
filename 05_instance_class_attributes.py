class Employee:
    company = "Google"
    salary = 100
harry = Employee()
rajani = Employee()

#creating instance attributes salary for both the objects
# harry.salary = 300
# rajani.salary = 400
harry.salary = 45
print(harry.salary)
print(rajani.salary)

#below line throws an error as address is not present in instance/class 
#print(rajni.address)