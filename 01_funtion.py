# marks1=[45,78,86,77]
# percentage1=(sum(marks1)/400)*100
# #or ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

# marks2=[75,98,88,78]
# percentage2=((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100
# print(percentage1,percentage2)

#using function
def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1=[45,78,86,77]
percentage1=percent(marks1)

marks2=[75,98,88,78]
percentage2=percent(marks2)

print(percentage1)
print(percentage2)

