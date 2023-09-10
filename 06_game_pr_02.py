def game():
    return 2345

score = game()
with open('C:\python program\9_Files\highscore.txt') as f:
    highscoreStr=(f.read())

if highscoreStr=='':
     with open("C:\python program\9_Files\highscore.txt",'w') as f:
        f.write(str(score)) 

elif int(highscoreStr)<score:
    with open("C:\python program\9_Files\highscore.txt",'w') as f:
        f.write(str(score))
