f=open('C:\python program\9_Files\poems.txt')
t=f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()
