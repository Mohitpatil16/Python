greeting="Good Morning,"
name="mohit"
print(greeting + name)
# concatenating two string
c=greeting+name
print(c)
name="mohit"
print(name[0])
print(name[4])
# name[3]='i'

print(name[0:4])  #string slicing
print(name[:4])   #it is same as name [0:4]
print(name[0:])   #show whole name
c=name[-4:-1]     #it is same as [1:4]
print(c)
name="MohitIsGood"
d=name[1:4:2]
print(d)