with open("C:\python program\9_Files\Mohit.txt") as f:
    content=f.read()

content=content.replace("donkey","!@#$%^&*")

with open("C:\python program\9_Files\Mohit.txt","w") as f:
    f.write(content)