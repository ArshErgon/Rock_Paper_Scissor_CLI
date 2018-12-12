
#   Still learning Python I love Python
#   If you find some problem or can make this code much better than please make so that I know where is gap in knowledge

#   THANK YOU!!!!!


from random import randint

choice = randint(1, 3)

if choice is 1:
    computerMove = "Rock"

elif choice is 2:
    computerMove = "Paper"

else:
    computerMove = "Scissor"

print(computerMove)
userMove = input("Enter Rock (r) Paper (p) Scissor (s)").lower()

if computerMove.lower() == "rock" and userMove.lower() == "r":
    userMove = "Rock"                                                                               #   Writing this UserMove again in "Rock" form beacuse I want my out to beautiful
    winner = f"Draw Computer plays \'{computerMove}\' and User plays \'{userMove}\'"                #   which let user to input First letter and when print it show the whole word

elif computerMove.lower() == "paper" and userMove.lower() == "p":
    userMove = "Paper"
    winner = f"Draw Computer plays \'{computerMove}\' and User plays \'{userMove}\'"

elif computerMove.lower() == "scissor" and userMove.lower() == "s":
    userMove = "Scissor"
    winner = f"Draw Computer plays \'{computerMove}\' and User plays \'{userMove}\'"

elif computerMove.lower() == "rock" and userMove.lower() == "p":
    userMove = "Paper"
    winner = f"User wins plays \'{userMove}\' over Computer\'s \'{computerMove}\'"

elif computerMove.lower() == "paper" and userMove.lower() == "r":
    userMove  = "Rock"
    winner = f"Computer wins plays \'{computerMove}\' over User\'s \'{userMove}\'"

elif computerMove.lower() == "scissor" and userMove.lower() == "p":
    userMove = "Paper"
    winner = f"Computer wins plays \'{computerMove}\' over User plays \'{userMove}\'"

elif computerMove.lower() == "paper" and userMove.lower() == "s":
    userMove = "Scissor"
    winner = f"User wins plays \'{userMove} over Computer plays \'{computerMove}\'"

elif computerMove.lower() == "rock" and userMove.lower() == "s":
    userMove = "Scissor"
    winner = f"Computer wins plays \'{computerMove}\' over User plays \'{userMove}\'"

elif computerMove.lower() == "scissor" and userMove.lower() == "rock":
    userMove = "Rock"
    winner = f"User wins plays \'{userMove}\' over Computer plays \'{computerMove}\'"

else:
    print(f"No this not allowed {userMove.capitalize()}")
try:                                                                        # 1. Using try because if the else comes True in winner variable nothing will store
    if winner[0] is "D":                                                    # 2. If I dont you the try function on this block it return error as NameError winner is not define
        print(winner)
except NameError:
    print("")
else:
    print("Doing Calculation")
    x = 10
    print('_____' * x)          # you can use a for loop in this section for print 2 lines i.e
    print('_____' * x)          # for i in range(2):
    print("\n", winner)         #     print("____"*x)
    print('_____' * x)
    print('_____' * x)
