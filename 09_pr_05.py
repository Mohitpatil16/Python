words=["donkey","kaddu","mote","chapri","mental"]

with open("C:\python program\9_Files\Mohit.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"!@#$%^&*")

with open("C:\python program\9_Files\Mohit.txt","w") as f:
    f.write(content)