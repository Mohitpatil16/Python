with open("C:\python program\9_Files\log.txt") as f:
    content=f.read()  #or we can use lower() here.

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("NO python is not present")

