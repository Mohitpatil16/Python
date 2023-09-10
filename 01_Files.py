#use open function function to read the content of the file
#f=open('Mohit.txt','r')  #we can give address of the file when file is not open via name
f=open('C:\python program\9_Files\Mohit.txt') #by default the mode is r.
# data=f.read()
data1=f.read(5)  #display first 5 characters

# print(data)
print(data1)

f.close()  #always close the file after completion of our work
