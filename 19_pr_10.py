#Python program to print multiplication table in reverse order
num=int(input("Enter any number:"))
i=10
for i in range(10,0,-1):
    print(f"{num}X{i}={num*i}")
    i=i-1
