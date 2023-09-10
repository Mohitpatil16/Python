file1="C:\python program\9_Files\s1.txt"
file2="C:\python program\9_Files\s2.txt"

with open(file1) as f:
    f1=f.read()

with open(file2) as f:
    f2=f.read()

if f1==f2:
    print("Files is identical")
else:
    print("Files are not identical")