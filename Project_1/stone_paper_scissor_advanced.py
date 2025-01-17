import random
import time

def stone_paper_scissor_game():
    print("WELCOME TO STONE PAPER SCISSOR 🎮")
    try:
        n = int(input("Enter the number of Rounds: "))
        if n <= 0:
            print("Number of rounds must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    myDict = {"stone": 1, "paper": 0, "scissor": -1}
    reverseDict = {1: "🪨 Stone", 0: "📄 Paper", -1: "✂️ Scissor"}

    ComputerWins = 0
    YourWins = 0

    for round in range(1, n + 1):
        print(f"\nRound {round}")
        myChoice = input("Enter your choice (stone/paper/scissor): ").lower()
        if myChoice not in myDict:
            print("Invalid choice. Please enter 'stone', 'paper', or 'scissor'.")
            continue

        print("Computer is choosing...", end="")
        computerChoice = random.choice([-1, 1, 0])
        time.sleep(5)
        print(f" Done! Computer chose: {reverseDict[computerChoice]}")

        result = (myDict[myChoice] - computerChoice) % 3
        if result == 0:
            print("It's a Draw!")
        elif result == 1:
            print("You win!")
            YourWins += 1
        else:
            print("Computer wins!")
            ComputerWins += 1

        print(f"Score: You {YourWins} - {ComputerWins} Computer")

    print("\nFINAL RESULT:")
    if YourWins > ComputerWins:
        print("🎉 Congratulations! You won the game!")
    elif YourWins < ComputerWins:
        print("😢 Sorry! Computer won the game!")
    else:
        print("🤝 It's a draw!")

    print("THANKS FOR PLAYING!")

if __name__ == "__main__":
    stone_paper_scissor_game()
