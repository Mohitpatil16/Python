letter='''Dear <|Name|>,Congratulations you're selected in our company.
We are excited to working with you.
Date:<|DATE|> '''
print(letter)
name=input("Enter your name:")
date=input("Enter date\n")
x="laughing"
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|DATE|>",date)
letter=letter.replace("working",x)
print(letter)