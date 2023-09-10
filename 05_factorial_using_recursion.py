def fact(n):
    if n==0:
        return(1)
    else:
        return(n*fact(n-1))           #eg-5!=5*4!

n=int(input("Enter the number:"))
result=fact(n)                        #function called
print("The factorial of",n,"is",result)