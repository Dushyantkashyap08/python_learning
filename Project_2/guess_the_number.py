import random

def play_game():
    print("Easy Level - 1 : (n:1-50)")
    print("Medium Level - 2 : (n:1-100)")
    print("Hard Level - 3 : (n:1-200)")

    level = int(input("Enter the difficulty level: "))

    if level == 1:
        n = random.randint(1, 50)
        max_attempts = 5
    elif level == 2:
        n = random.randint(1, 100)
        max_attempts = 8
    elif level == 3:
        n = random.randint(1, 200)
        max_attempts = 12
    else:
        print("Default level: Medium")
        n = random.randint(1, 100)
        max_attempts = 8

    print(f"\nYou have {max_attempts} attempts to guess the number. Good luck!\n")

    attempt = 0

    while attempt < max_attempts:
        attempt += 1
        print(f"Attempt {attempt}/{max_attempts}")

        num = int(input("Enter your guess: "))

        if num < 0:
            print("Enter a number in range please.")
            continue

        if num == n:
            print(f"🎉 Congratulations! You guessed the number {n} in {attempt} attempts!")
            break

        if num > n:
            print("Guess a lower number, please.")
        else:
            print("Guess a higher number, please.")

        # Hint system
        difference = abs(num - n)
        if difference <= 5:
            print("🔥 You are very close!")
        elif difference <= 10:
            print("⚡ You are getting closer.")
        else:
            print("📉 You are far off. Try again.")

    else:
        print(f"❌ Sorry, you've run out of attempts! The correct number was {n}. GAME OVER.")

    # Play again system
    play_again = input("Do you want to play again (yes/no)? ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing....Goodbye!")


# Play the game
play_game()
