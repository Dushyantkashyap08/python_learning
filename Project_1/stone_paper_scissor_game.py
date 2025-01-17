#stone paper scissor game
import random

'''
1: stone
0: paper
-1: scissor
'''

print("WELCOME TO STONE PAPER SCISSOR")

n = input("Enter the number of Rounds: ")

round = 1
ComputerWins = 0
YourWins = 0

while round <= int(n):
    print(f"Round {round}")
    
    myChoice = input("enter your choice: ")
    myDict = {
        "stone": 1,
        "paper": 0,
        "scissor": -1
    }
    reverseDict = {
        1: "stone",
        0: "paper",
        -1: "scissor"
    }

    computerChoice = random.choice([-1, 1, 0])
    print(f"You chose : {myChoice} and computer chose : {reverseDict[computerChoice]}")

    if myDict[myChoice] == computerChoice:
        print("It's a Draw")
        round += 1
    else: 
        if computerChoice == -1 and myDict[myChoice] == 1:
            print("You win")
            YourWins += 1
            
        elif computerChoice == -1 and myDict[myChoice] == 0:
            print("Computer win")
            ComputerWins += 1
            
        elif computerChoice == 1 and myDict[myChoice] == -1:
            print("Computer win")
            ComputerWins += 1
        
        elif computerChoice == 1 and myDict[myChoice] == 0:
            print("You win")
            YourWins += 1

        elif computerChoice == 0 and myDict[myChoice] == -1:
            print("You win")
            YourWins += 1

        elif computerChoice == 0 and myDict[myChoice] == 1:
            print("Computer win")
            ComputerWins += 1
            
        else:
            print("Something went wrong")
        
        round += 1

if YourWins > ComputerWins:
    print("You won the game")
elif YourWins < ComputerWins:
    print("Computer won the game")
else:
    print("It's a draw")
        
print("THANKS FOR PLAYING...")
