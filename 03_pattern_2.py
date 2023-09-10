n=int(input("Enter the number of rows:"))
for row in range(n):
    for col in range(n):
        if col==0 or (row==col) or (row==n-1):
            print("*",end="")         #end="" for control remains in same line
        else:
            print(end=" ")            #end=" " for print space
    print()