# Rock Paper Scissors Game
import random

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input(
            "Enter your choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Rock crushes scissors! You win!")
    elif player == "paper" and computer == "rock":
        print("Paper covers rock! You win!")
    elif player == "scissors" and computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("You lose! Better luck next time.")
    # Ask the player if they want to play again
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        running = False
        print("Thanks for playing!")
