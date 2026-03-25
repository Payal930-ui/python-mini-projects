import random
target = random.randint(1,100)

while True:
    userChhoice=int(input("Guess The Target or Quit(Q): "))
    if (userChhoice=="Q"):
         break              
    userChhoice=int(userChhoice)
    if(userChhoice==target):
        print("success:correct guess") 
        break
    elif(userChhoice<target):
        print("Your no. is too small,Guess bigger....")
    else:
        print("Your no. is too big,Guess smaller....") 


print("_____GAME OVER_______" )                              

