content=True
i=0

with open("C:\python program\9_Files\log.txt") as f:
    
    while content:
        i+=1
        content=f.readline()  #readline reads the lines
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
            print(i)
        