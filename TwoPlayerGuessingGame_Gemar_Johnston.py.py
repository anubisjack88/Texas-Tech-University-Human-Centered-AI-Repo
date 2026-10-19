import random

# Generate the secret number the player and computer are both trying to guess
secret_number = random.randint(1, 20)

# Tracks the current round number
round_number = 1

print("Welcome to Johnston's Guessing Game! It's you vs a computer. Who will win? Good luck! I'm thinking of a number between 1 and 20.")
print("You and the computer will take turns guessing until a player is correct.\n")

while True:
    print(f"--- Round {round_number} ---")

    # 1. Human's turn to guess (now protected against bad input)
    try:
        user_guess = int(input("Your guess: "))
    except ValueError:
        print("That's not a valid number. Please enter a whole number between 1 and 20.\n")
        continue  # skip the rest of this round and re-prompt

    if user_guess == secret_number:
        print(f"You guessed it! The secret number was {secret_number}.")
        print("YOU WIN!")
        break
    elif user_guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    # -------------------------------------------
    # 2. Computer's turn to guess
    computer_guess = random.randint(1, 20)
    print(f"Computer guesses: {computer_guess}")

    if computer_guess == secret_number:
        print(f"The computer guessed it right! The secret number was {secret_number}.")
        print("COMPUTER WINS!")
        break
    elif computer_guess < secret_number:
        print("Computer's guess was too low.")
    else:
        print("Computer's guess was too high.")

    print()  # blank line for readability
    round_number += 1

print("\nThanks for playing!")

# Keeps the console window open until the user is ready to close it.
#I found that I needed input validation and I did not have a pause at the end of the program leading to it crashing.
#This is my refactored code.
input("Press Enter to exit...")
 
