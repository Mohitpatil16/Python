class Number:
    def __init__(self,num):                                                             #__init__ is dunder method
        self.num = num

    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num
    def __mul__(self,num2):
        print("Lets multiply")
        return self.num * num2.num


n1 = Number(4)
n2 = Number(6)
sum = n1+n2
mul = n1*n2
print(sum)
print(mul)

#imp for operator overloading:

# for p1+p2 --> p1 __add__(p1)
# for p1-p2 --> p1 __sub__(p2)