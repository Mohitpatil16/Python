n=int(input("Enter the number:"))
result=1
for i in range(n,0,-1):    #n=start,0=end,-1= is the stepsize i.e nos are printed in reverse order
    result=result*i
print("The factorial of",n,"is",result)