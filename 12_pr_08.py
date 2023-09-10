
with open("C:\python program\9_Files\this.txt") as f:
    content=f.read()

with open("copy.txt",'w') as f:
    f.write(content)