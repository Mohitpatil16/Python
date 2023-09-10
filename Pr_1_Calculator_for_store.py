# Write a python program which keep adding a stream of numbers inputed by the user
sum=0
while(True):
    userInput=input("Enter the price:\n")
    if(userInput!='q'):
        sum=sum+int(userInput)
        print(f"Your order total so far:{sum}")
    else:
        print("Thank you for using our calculator")
        print(f"Your bill total is {sum}.Thanks for shopping with us")
        break