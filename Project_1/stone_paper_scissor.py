#stone paper scissor game
import random

'''
1: stone
0: paper
-1: scissor
'''

print("WELCOME TO STONE PAPER SCISSOR GAME")
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
else: 
    if computerChoice == -1 and myDict[myChoice] == 1:
        print("You win")
    elif computerChoice == -1 and myDict[myChoice] == 0:
        print("Computer win")
    elif computerChoice == 1 and myDict[myChoice] == -1:
        print("Computer win")
    elif computerChoice == 1 and myDict[myChoice] == 0:
        print("You win")
    elif computerChoice == 0 and myDict[myChoice] == -1:
        print("You win")
    elif computerChoice == 0 and myDict[myChoice] == 1:
        print("Computer win")
    else:
        print("Something went wrong")
