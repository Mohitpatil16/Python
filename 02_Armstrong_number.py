#153
#There are 3 digits in this number therefore n=3
#find the third power of each number and take sum of it.if 
#it is equal to actual number then the given no is armstrong number
#153=1^3+5^3+3^3=153

for i in range(1001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10       #//trunketed division
    if num==result:
        print(num)