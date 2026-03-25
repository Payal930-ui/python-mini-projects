import random 
item=["rock","scissor","paper"]
userchoice=input("enter your move=Rock,Scissor,Paper: ")
computerchoice=random.choice(item)
print(f"our User choiceis:{userchoice }, our computer choices: ,{computerchoice}") 
if computerchoice==userchoice:
    print("It's a tie")
else:
    if(userchoice=="rock" and computerchoice=="scissor"):
        print("our user will win ")
    elif(userchoice=="rock" and computerchoice=="paper") :
        print("Our computer wins...")
    elif(userchoice=="scissor" and computerchoice=="paper"):
        print("our user will win ")
    elif(userchoice=="scissor" and computerchoice=="rock") :
        print("Our computer wins...")
    elif(userchoice=="paper" and computerchoice=="rock"):
        print("our user will win ")
    elif(userchoice=="paper" and computerchoice=="scissor") :
        print("Our computer wins...")    
    else:
        print("something wrong")    